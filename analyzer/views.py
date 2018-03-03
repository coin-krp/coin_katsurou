# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import MongoClient
import analyzer.server_config as config

# Create your views here.

def index(request):
    client = MongoClient(config.mongoserver, 27017, username=config.mongoid, password=config.mongopw)
    db_names = client.database_names()
    context = {}
    return render(request, 'analyzer/index.html', {})

