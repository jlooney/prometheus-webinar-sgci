What is Prometheus?
===================

https://prometheus.io/docs/introduction/overview/

Prometheus allows you to create and use time-series metrics for monitoring, alerting, and graphing.


## Features of Prometheus:

- open source
- uses time-series data
- metrics are specified with a name and key/value pairs
- uses a query language, PromQL, to allow you to create more flexible monitoring 
- data collection for the time series data occurs over HTTP
- contains a graphing dashboard and is also compatible with other open source graphing tools such as Grafana




## Components:
1. Prometheus Server
2. Jobs/Applications
3. Alert manager
4. Data visualization 


#### Prometheus Server
The prometheus application itself. Runs on an HTTP Server and scrapes metrics from the specified targets.

#### Jobs/Applications
Anything that generates metrics for prometheus to scrape. Prometheus uses HTTP to scrape an endpoint for the job or application. 

For short-lived jobs, a pushgateway can be used. For time-series metrics, the standard scraping is used. 

#### Alert Manager
Alerts can be set up using PromQL queries. When one of the alerts is 'fired', the alert manager can be set up to send alerts. These alerts can be sent to various applications such as Slack or HipChat.

#### Data visualization
Prometheus comes equipped with a basic graphing dashboard that works with PromQL queries. Additionally, services such as Grafana can be easily integrated with Prometheus for more advanced data visualizations. 



### In this webinar:
In this webinar we will cover setting up the Prometheus Server to scrape an application for metrics, which it will then save to its time-series database. We will also look a bit at the Prometheus Dashboard. 



























--