from maze.maze import Maze
from servers import ServerManager
import json
import requests

MIDDLEWARE_URL = "http://sp22-cs240-adm.cs.illinois.edu:24000"

response = requests.get(f'{MIDDLEWARE_URL}/listMG')

if response.status_code//100 != 2:
    print(response.data)
    exit(1)

mgs = response.json()

for key in mgs:
    mg = mgs[key]
    
    url = mg["url"]

    if "127.0.0.1" in url or 'localhost' in url:
        deleteResponse = requests.delete(f'{MIDDLEWARE_URL}/deleteMG/{key}')
        print("Delete MG: " + str(deleteResponse.status_code) + ":" + str(deleteResponse.data))

    if mg['author'] != 'zpzhang2' or mg['author'] != 'aaryab2':
        deleteResponse = requests.delete(f'{MIDDLEWARE_URL}/deleteMG/{key}')
        print("Delete MG: " + str(deleteResponse.status_code))