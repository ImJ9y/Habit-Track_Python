import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "jgaiang123"
USERNAME = "jayim"
GRAPH_ID = "graph1"

user_params = {
    "token": f"{TOKEN}",
    "username": f"{USERNAME}",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",  # Removed the extra colon here
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": f"{GRAPH_ID}",
    "name":"Running Graph ",
    "unit":"km",
    "type":"float",
    "color":"kuro"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# cur_date = str(datetime.datetime.today().date()).replace("-","")

today = datetime.datetime.now()

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
add_pixel_params = {
    "date": f"{today.strftime("%Y%m%d")}",
    "quantity": input("How many kilometers did you run today?"),
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
# print(response.text)


update_pixel_endpoint = f"{add_pixel_endpoint}/{today.strftime("%Y%m%d")}"
update_pixel_params = {
    "quantity":"12.00",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
print(response.text)



