Location Extractor
====================================

This module extracts country from states in text content. It requires pycountry for analysis. 




##Examples:
```python
from locationExtractor import locationExtractor

print locationExtractor.detect("I live in New York")
>>> {'city': 'new york', 'code': u'US', 'country': u'United States'}
 
 
print locationExtractor.detect("ankara")
>>> {'city': 'ankara', 'code': u'TR', 'country': u'Turkey'}

``` 

If you want to change memcache host;
```python
locationExtractor.Locations.memcacheHost = "Your Host"
```

But when you did this changes for memcachehost, You must init manually for this condition.

```python
locationEXtractor.Location.init()
```

  
