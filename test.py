import requests
response = requests.get("https://www.google.com/").status_code
print(response)
response = int(str(response))
list_num = []
while response>0:
    count = response%10
    list_num.append(count)
    response = response//10
if list_num[len(list_num)-1]==2:
    print("yes")
