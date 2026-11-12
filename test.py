import requests
print("Hello, Welcome to your website checker!")
print("Sample : https://www.google.com/")
response = requests.get("https://www.google.com/").status_code
print(response)
response = int(str(response))
list_num = []
while response>0:
    count = response%10
    list_num.append(count)
    response = response//10
if list_num[len(list_num)-1]==2:
    print("Yes, this website is working!")
elif list_num[len(list_num)-1]==1:
    print("Hold on, the website has a problem on the server")
elif list_num[len(list_num)-1] == 3:
    print("You have no permission to access this website")
elif list_num[len(list_num)-1]==4:
    print("There are some errors occured from your side!")
elif list_num[len(list_num)-1]==5:
    print("There has been a problem from the server's side")
else:
    print("Website unidentified")
