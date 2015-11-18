#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    trends api
    ~~~~~~~~    
    :copyright: (c) 2015 by basilboli
"""

from flask import Flask, request, redirect, render_template, url_for, flash, abort, session, g, flash,_app_ctx_stack
import json,redis

redis = redis.StrictRedis(host="localhost", port=6379, db=0)
app = Flask(__name__)

@app.route('/trends')
def trends():    
    items = redis.lrange("rawdata.trends", 0, -1)    
    print items
    return json.dumps(items)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)    

