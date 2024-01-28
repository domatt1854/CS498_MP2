import requests

domain = 'http://127.0.0.1:5000/'

response = requests.get(domain)
print(str(response.content))
response = requests.post(domain, json = {'num': 100})
print(str(response.content))
response = requests.get(domain)
print(str(response.content))


response = requests.post(domain, json = {'num': 500})
print(str(response.content))
response = requests.get(domain)
print(str(response.content))
