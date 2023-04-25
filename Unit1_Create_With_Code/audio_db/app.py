import requests

url = "https://theaudiodb.com/api/v1/json/{APIKEY}/searchalbum.php"

querystring = {"s":"daft_punk"}

headers = {
	"X-RapidAPI-Key": "523532",
	"X-RapidAPI-Host": "theaudiodb.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)