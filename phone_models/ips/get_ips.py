import json

with open('Free_Proxy_List.json', 'r') as file:
    data = json.load(file)

    with open('proxies.txt', 'w+') as pf:
        for i in data:
            pf.write(i['ip'] + '\n')
