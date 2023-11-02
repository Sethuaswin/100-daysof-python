import requests
from datetime import datetime

USER_NAME = "sethuaswin"
TOKEN = "5h4543hto234uoi23kfnefnc"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# request.post() used to provide information to the external system,
# which in this case pixela

# STEP-1: Create Username and Password

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP-2: Create a graph

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

# headers is secure way to provide API Key
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
#     )
# print(response.text)

# STEP-3: Post a value to the Graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How Much time you have Meditated Today?: ")
}

response = requests.post(
    url=pixel_creation_endpoint,
    json=pixel_data,
    headers=headers
)

print(response.text)
# print(today.strftime("%Y%m%d"))

# STEP-4: Updating a data poind
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"  # noqa
new_pixel_data = {
    "quantity": "15.0"
}

# response = requests.put(
#     url=update_endpoint,
#     json=new_pixel_data,
#     headers=headers
# )

# print(response.text)

# STEP-5: Deleting a pixel

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"  # noqa
# response = requests.delete(
#     url=delete_endpoint,
#     headers=headers
# )
# print(response.text)
