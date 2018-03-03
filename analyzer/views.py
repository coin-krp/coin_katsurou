# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import MongoClient
import analyzer.server_config as config
import datetime
# Create your views here.

def index(request):
    client = MongoClient('localhost', 27017, username=config.mongoid, password=config.mongopw)
    db_names = client.database_names()
    context = {}

    db = client.gekko
    poloniex_prices = db.poloniex_prices

    price_data = {}
    for poloniex_price in poloniex_prices.find():
        p_time = datetime.datetime.utcfromtimestamp(poloniex_price['start']).strftime('%Y-%m-%dT%H:%M:%SZ')
        price_data[p_time] = poloniex_price['close'] 
    
    context['price_count'] =  poloniex_prices.count()
    context['price_data'] =  price_data

    return render(request, 'analyzer/index.html', context)
    #return HttpResponse(db_names[0])

