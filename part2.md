What are metrics?
=================
Prometheus features 4 core metric types. 


## Counter
Counters can be increased, or reset to 0. They can only be incremented.

## Gauge
Gauges can be incremented or decremented

## Histogram
Samples observations. Provides 3 datapoints per scrape:
- a cumulative counter for observations over a specified time
- total sum of all observed values
- count of all events that have been observed 

## Summary
Similar to Histogram, but calculates configurable quantiles over a specific window of time.
Provides 3 data points per scrape:
- streaming quantiles
- total sum of all observed values
- count of all events that have been observed

 

