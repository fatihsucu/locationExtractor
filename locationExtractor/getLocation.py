# -*- coding: utf-8 -*-
import pycountry
from data.memcachedStates import*

def detectPlace(source):	
 	country = Memcached.getLocate(source)
 	if country != None:
 		result = pycountry.countries.get(alpha2=country)
 		return result.name
 	else:
 		return None
 	



print detectPlace("bizim Mexico bazı şeylerin öyle olması gerekir bizim ora ")