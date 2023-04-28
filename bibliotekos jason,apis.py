import random

import requests
from pprint import pprint
import json
# duomenys = requests.get("https://opentdb.com/api.php?amount=10")
# print(duomenys.text)



duomenys_json = requests.get("https://opentdb.com/api.php?amount=10")
# print(duomenys_json.status_code)
# print(duomenys_json.content)

duomenys = json.loads(duomenys_json.text)

pprint(duomenys)

# '''
# jason
# '''
#
# data = '''{
#   "student": [
#
#      {
#         "id":"01",
#         "name": "Tom",
#         "lastname": "Price"
#      },
#
#      {
#         "id":"02",
#         "name": "Nick",
#         "lastname": "Thameson"
#      }
#   ]
# }'''
# duomenys = json.loads(data)
#
# pprint(duomenys)
#
# studentai = duomenys["student"]
#
# for studentas in studentai:
#     print(studentas["name"])
#     studentas["year"] = random.randint(1, 4)
#
# pprint(duomenys)
#
# json_duomenys = json.dumps(duomenys)#cia vel pavercia i json formata
#
# print(type(json_duomenys))
#
# print(json_duomenys)
