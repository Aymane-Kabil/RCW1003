import requests

#url ='http://localhost:8000/test'
url = 'https://rcw1003-instant1-g2bpfaena8gjbdfs.canadaeast-01.azurewebsites.net/'
response =requests.get(url)
response = response.json()
print(response['message'])