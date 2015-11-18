#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    trends api
    ~~~~~~~~    
    :copyright: (c) 2015 by basilboli
"""

from flask import Flask
import json, redis
import settings

redis = redis.StrictRedis(host="localhost", port=6379, db=0)
app = Flask(__name__)

@app.route('/trends')
def trends():    
    items = redis.lrange(settings.channel, 0, -1)    
    print items
    return json.dumps(items)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)    

