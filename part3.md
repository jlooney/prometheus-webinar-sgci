Creating Metrics with Python
==

##The python Prometheus package

There is a python package called `prometheus_client` that can be pip installed. 

https://github.com/prometheus/client_python

```pip install prometheus_client```

##Setting up basic metrics

Using `prometheus_client`, we can create metric objects that prometheus can scrape. All four metric types can be created.

####Counter:
```python
from prometheus_client import Counter
c = Counter('num_requests', 'The number of requests.')
c.inc() # Increments the counter by 1
c.inc(10) # Increments the counter by 10

```

####Gauge:
```python
from prometheus_client import Gauge
g = Gauge('memory_in_gb', 'The amount of memory remaining on this server in GB.')
g.inc() # Increments the gauge by 1
g.dec() # Decrements the gauge by 1
g.set(6.3) # Sets the gauge to an exact value

```

###Histogram:
```python
from prometheus_client import Histogram
h = Histogram('request_latency_seconds', 'Description of histogram')
h.observe(2.5)    # Observe the number of seconds
```

####Summary:
```python
from prometheus_client import Summary
s = Summary('request_latency_seconds', 'The request latency in seconds.')
s.observe(3.7)    # Observe the number of seconds
```

Note: the python prometheus client cannot store quantile information yet. 


##Adding labels
Labels can also be added to metrics for easier querying. Labels will group together all data points with that given label.
To add a label, it will be specified when the metric object is created:
```python
from prometheus_client import Gauge
g = Gauge(
    'memory_in_gb', 
    'The amount of memory remaining on this server in GB.',
    ['server_name'] # name of the label
)
# When we set a value ofh a labelled metric, 
# we need to specify which label is getting that value
g.labels('server1').set(6.3) 
g.labels('server2').set(2.8)

```

Later when we query the 'memory_in_gb' metric, we will have one gauge listing for each server we specified.

##Generating metrics plaintext

In order to scrape and collect metrics, Prometheus needs the metrics to appear in a specific format. Example:
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 1.693277e+06
python_gc_objects_collected_total{generation="1"} 4.99867e+06
python_gc_objects_collected_total{generation="2"} 467275.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 285137.0
python_gc_collections_total{generation="1"} 25921.0
python_gc_collections_total{generation="2"} 1240.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="2",version="3.7.2"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.668186112e+09
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 4.4384256e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.55535539383e+09
```

The Prometheus python library includes a function (`generate_latest()`) that will turn all of the metrics objects into the plaintext format that Prometheus needs to scrape. 

For example, if you are returning all your metrics in a function, you could return this:
```python
return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
```


