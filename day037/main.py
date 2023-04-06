import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "rakshitdabral"
token = "ahshshasdnjksabdkjab2"
graph_id = "graph1"

user_para = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_para)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id" : graph_id,
    "name": "Studying",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

header = {
    "X-USER-TOKEN" : token,
}

# response = requests.post(url=graph_endpoint, json=graph_config,headers=header)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.datetime(2023, 4, 3)
date_today = today.strftime("%Y%m%d")
pixel_config = {
    "date": date_today,
    "quantity" : "1",
}

# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=header)
# print(response.text)

piexl_update_endpoint = f"{pixel_endpoint}/{date_today}"

pixel_update_config = {
    "quantity" : "2",
}
response = requests.put(url=piexl_update_endpoint, json=pixel_update_config, headers=header)
print(response.text)