import requests
response = requests.get("https://www.google.com/").status_code
print(response)
response = int(str(response))
