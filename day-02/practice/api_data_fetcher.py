import requests

input = input("How do you like you coffee? hot or iced...")

url = f"https://api.sampleapis.com/coffee/{input}"
response = requests.get(url= url)


for item in response.json():
    for key,values in item.items():
        if(key == "id" and values == '_nZxs9J'):
            with open("file.txt", "w") as f:
                f.write(key)

print(type(response.json()))