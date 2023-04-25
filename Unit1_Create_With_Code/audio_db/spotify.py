import json
import requests

url = "https://spotify23.p.rapidapi.com/tracks/"

querystring = {"ids":"4WNcduiCmDNfmTEz7JvmLv"}

headers = {
	"X-RapidAPI-Key": "bd06bb2382msh874e76e6ff29000p12bc4djsn26abdf362181",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(type(response.text))
print(response.text)
source = response.text
print(type(source))
print(source)
data = json.loads(source)
print(type(data))
print(data)
print(data.keys())
print(data['tracks'])

for item in data['tracks']:
    #print(item['eternal_urls']['name'])
	print(item['external_urls']['spotify'])
	print(item['name'])
	print(item['artists'][0]['name'])
	for item in item['artists']:
		print(item['name'])