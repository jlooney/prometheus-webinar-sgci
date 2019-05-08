from flask import Flask, send_file, request, Response
from prometheus_client import start_http_server, Counter, generate_latest, Gauge
import docker
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

users_per_worker = Gauge(
    'number_of_users_on_this_worker',
    'The number of users with notebook servers on this worker.'
)

my_basic_counter = Counter(
    'my_basic_counter',
    'A basic counter.'
)

@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""

    my_basic_counter.inc()


    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')