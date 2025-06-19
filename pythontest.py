import requests

url = "https://3eurotools.it/models-info"
params = {
    "company": "google",
}

response = requests.get(url, params=params)
print(response.text)
