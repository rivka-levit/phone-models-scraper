import json
import requests

r = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page='
                 '1&sort_by=lastChecked&sort_type=desc')

data = json.loads(r.text)

with open('proxies.txt', 'w+') as pf:
    for i in data['data']:
        pf.write(i['ip'] + '\n')
