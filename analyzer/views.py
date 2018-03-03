# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import MongoClient
import analyzer.server_config as config
import datetime
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'analyzer/index.html', {})

def get_price(request):
    client = MongoClient(config.mongoserver, 27017, username=config.mongoid, password=config.mongopw)
    db_names = client.database_names()
    context = {}

    db = client.gekko
    poloniex_prices = db.poloniex_prices
    
    price_data = []
    for poloniex_price in poloniex_prices.find().sort('start',pymongo.DESCENDING).limit(100):
        p_time = datetime.datetime.utcfromtimestamp(poloniex_price['start']).strftime('%Y-%m-%dT%H:%M:%SZ')
        price_data.append([p_time,poloniex_price['close'],poloniex_price['start']])

    min_price_time = price_data[-1][2]

    poloniex_adivces = db.poloniex_advices
    
    advice_data = []
    for poloniex_advice in poloniex_adivces.find().sort('time',pymongo.DESCENDING):
        p_time = datetime.datetime.utcfromtimestamp(poloniex_advice['time']).strftime('%Y-%m-%dT%H:%M:%SZ')
        if min_price_time > poloniex_advice['time']:
            break
        advice_data.append([p_time,poloniex_advice['recommendation']])

    context['min_price_time'] = min_price_time
    context['min_price_time2'] = poloniex_advice['time']

    context['price_count'] =  poloniex_prices.count()
    context['price_data'] =  price_data
    context['advice_data'] =  advice_data

    #return HttpResponse(db_names[0])
    return JsonResponse(context)