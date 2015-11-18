#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    trends
    ~~~~~~~~    
    :copyright: (c) 2015 by basilboli
"""

import redis
import re
import settings

channel = settings.channel
stream_host = settings.stream_host

def bad (term): 
    bad = len(term) <= 1 
    bad = bad or re.search("\D", term) is None
    bad = bad or re.search(settings.exclude_regex, term) is not None
    return bad

if __name__ == '__main__':
    

    stream = redis.StrictRedis(host=stream_host, port=6379, db=0)        
    redis = redis.StrictRedis(host="localhost", port=6379, db=0)        
    ps = stream.pubsub()
    ps.subscribe([channel])
    print "Subcribed to ", channel

    for item in ps.listen():
        if item['type'] == 'message':
            i = item['data'].strip()
            # print "Received ", item['data']
            if not bad(i): 
                items = redis.lrange(channel, 0, -1)    
                if not i in items:
                    print "Added ", i
                    redis.ltrim(channel, 0, 20)
                    redis.lpush(channel, i)
            else :
                print "Ignored", i        
