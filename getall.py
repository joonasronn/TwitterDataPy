# -*- coding: utf-8 -*-
import requests
#Use this for recieving data from your API
resp = requests.get('##your api here##')
if resp.status_code != 200:
    #Joku meni pieleen
    raise ApiError('get error {}'.format(resp.status_code))
for item in resp.json():
    print('{} {}'.format(item['name'], item['text']))