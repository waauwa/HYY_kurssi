#Code to access data with token
import requests
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


items_list = []
url = 'https://api.vk.com/method/groups.getMembers'

for i in range(0,x,100):
    params = dict(
            group_id ='xxx',
            count = 100,
            offset = i,
            fields = "sex, city, country, online, bdate, contacts, last_seen, listscontacts, connections, site, education, universities, schools,lists",
            v = '5.78',
            access_token='xxx'
            )
    resp = requests.get(url=url, params=params)
    resp_json = resp.json()
    items = resp_json.get("response").get("items")
    items_list.append(items)
    

flat_item_list = []

for sublist in items_list:
    for item in sublist:
        flat_item_list.append(item)


nomrmalized_items = json_normalize(flat_item_list)
test_df = pd.DataFrame.from_dict(nomrmalized_items)  

test_df.to_csv(path_or_buf=r"C:\path.csv", sep=';', encoding="UTF8")
print(resp)