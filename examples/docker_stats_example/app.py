from flask import Flask, send_file, request, Response
from prometheus_client import start_http_server, Counter, generate_latest, Gauge
import docker
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
MBFACTOR = float(1 << 20)

memory_gauge = Gauge(
    'memory_usage_in_mb',
    'Amount of memory in megabytes currently in use by this container.',
    ['name']
)

client = docker.from_env(version='1.23')


@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""
    containers = client.containers.list()
    for container in containers:
        name = container.name

        # Get memory data for this container
        try:
            with open('/docker/memory/{}/memory.usage_in_bytes'.format(container.id), 'r') as memfile:
                memory = memfile.read()
                memory = int(memory) / MBFACTOR
                memory_gauge.labels(name).set(memory)
        except Exception as e:
            logger.error("Failed to update memory metric. Exception: {}".format(e))

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
