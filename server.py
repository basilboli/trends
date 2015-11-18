#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    trends
    ~~~~~~~~    
    :copyright: (c) 2015 by basilboli
"""

import redis
import re

def bad (term): 
    bad = len(term) < 1 
    bad = bad or "not provided" in term 
    bad = bad or term=="-" 
    bad = bad or "http://" in term
    bad = bad or re.search("\D", term) is None
    bad = bad or re.search("3suisses|suisse|3\ssuisses|trois\ssuisse", term) is not None
    return bad

if __name__ == '__main__':

    # print bad ("3suisses")
    # print bad ("tasses petit dejeuner")
    # print bad ("1234324")

    stream = redis.StrictRedis(host="address", port=6379, db=0)        
    redis = redis.StrictRedis(host="localhost", port=6379, db=0)        

    channel = "rawdata.trends"
    ps = stream.pubsub()
    ps.subscribe([channel])
    print "Subcribed to ", channel

    for item in ps.listen():
        if item['type'] == 'message':
            i = item['data'].strip()
            # print "Received ", item['data']
            if not bad(i): 
                items = redis.lrange("rawdata.trends", 0, -1)    
                if not i in items:
                    print "Added ", i
                    redis.ltrim(channel, 0, 20)
                    redis.lpush(channel, i)
            else :
                print "Ignored", i        
