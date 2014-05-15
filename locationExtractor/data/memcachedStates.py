# -*- coding: utf-8 -*-
import re 
import memcache
import pickle
import os
import itertools

class Memcached(object):
    """
    
    """

    memcacheHost = '127.0.0.1:11211'
    mcclient = memcache.Client([memcacheHost], debug=0)
    isInitialized = None
    xxx=0
    collectionSourceFile = 'cache'
    collectionName = 'cities'
    collection = None

    @classmethod
    def init(cls):
        cls.collection = cls.cache_retrieve(cls.collectionName)
        if not cls.collection:
            items = cls.loadFromSource()
            cls.cache_store(cls.collectionName, items)
        cls.isInitialized = True

    @classmethod
    def cache_store(cls, key, value, chunksize=950000):
      serialized = pickle.dumps(value, 2)
      values = {}
      for i in xrange(0, len(serialized), chunksize):
        values['%s.%s' % (key, i//chunksize)] = serialized[i : i+chunksize]
      cls.mcclient.set_multi(values)
    
    @classmethod
    def cache_retrieve(cls, key):
        result = cls.mcclient.get_multi(['%s.%s' % (key, i) for i in xrange(32)])
        serialized = ''.join([v for v in result.values() if v is not None])
        if serialized:
            return pickle.loads(serialized)
        else:
            return None

    @classmethod
    def loadFromSource(cls):       
        with open("cache","rb") as f:
            cities = pickle.load(f)
        return cities

    @classmethod
    def getLocate(cls, source):
        if not cls.isInitialized:
            cls.init()
        
        tokens = re.compile("[ '?.;,-/]").split(source.lower())
        combines = itertools.combinations(tokens,2)
        possibleCombines = list(combines)
        for combine in possibleCombines:
            string = " ".join(combine)
            try:
                return cls.collection[string].upper()
            except:
                pass

        for token in tokens:
            try:
                return cls.collection[token].upper()
            except:
                pass
 
        
        
