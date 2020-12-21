import requests
import json

url = "https://trains.p.rapidapi.com/"

def getTrainData(t_name):

    payload = "{\r\n\"search\": \""+t_name+"\"\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "147ad3c377msh7e3e8874f7841a6p1dfffajsna5a2fe798fd3",
        'x-rapidapi-host': "trains.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)

    return result
