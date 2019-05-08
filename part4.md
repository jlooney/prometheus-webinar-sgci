Configuring Prometheus to scrape metrics
===


####Prometheus Config file
In order for Prometheus to scrape and collect metrics, it needs a configuration file. This file will specify the locations it will scrape for mertrics. At the very basic level, Prometheus will scrape itself.

This configuration file is written in YAML: 
```yaml
global:
    scrape_interval: 5s
    external_labels:
        monitor: 'my-monitor'

scrape_configs:
    - job_name: 'prometheus'
      static_configs:
        - targets: ['localhost:9090']
```

This is the most basic implementation of prometheus, where it will just scrape the metrics that it produces about itself. 

The first thing we can specify is the interval of time between each scrape. The default is 5 seconds, but this can be any value.

Next we set up the scrape configs. Each job under the configs represents a target that Prometheus will scrape. In this example we only have one, which is the prometheus service itself. All we need to do is give the job a name and then provide an IP address where the plaintext is located.

####Deploying Prometheus
To deploy Prometheus, we will be using Docker. Prometheus has its own official Docker image, so all we will need to do is tell it to use our config file.

To make things easier, we will use docker-compose, which uses YAML:

```yaml
prom:
    image: prom/prometheus:v2.1.0
    volumes:
        - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
        - '--config.file=/etc/prometheus/prometheus.yml'
        - '--storage.tsdb.path=/prometheus'
    ports:
- '9090:9090'
```

