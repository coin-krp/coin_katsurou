# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import MongoClient


# Create your views here.

"""
def index(request):
    client = MongoClient('localhost', 27017, username='krp', password='krp1234567890!')
    db_names = client.database_names()
    return HttpResponse(db_names[0])
"""
def index(request):
    client = MongoClient('localhost', 27017, username='krp', password='krp1234567890!')
    db_names = client.database_names()
    context = {}
    return render(request, 'ananlyzer/index.html')

