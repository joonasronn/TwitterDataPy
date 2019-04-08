# -*- coding: utf-8 -*-
import requests
import csv
import json

def upload(nimi):
    f = open(nimi +"_tweets.csv", 'r')
    reader = csv.DictReader(f)  
    jsondata = json.dumps( [ row for row in reader ] ) 
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    r = requests.post("###Yourapihere###", data=jsondata, headers=headers, verify=False)
    print(r.status_code, r.reason)

    print(jsondata)