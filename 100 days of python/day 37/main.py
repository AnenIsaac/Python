import requests 
from datetime import date
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "anen"
TOKEN = "somerandomtoken123."
# Creating a user in pixela
user_params = {
    "token" : TOKEN, 
    "username" : USERNAME, 
    "agreeTermsOfService" : "yes", 
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN" : TOKEN,
}

graph_params = {
    "X-USER-TOKEN" : TOKEN, 
    "id" : "readinggraph", 
    "name" : "Reading", 
    "unit" : "minutes", 
    "type" : "int",
    "color" : "sora"
}

# graph_response = requests.post(url=graph_endpoint, headers=header, json=graph_params)
# print(graph_response.text)

# Post data on to the graph
graphID = "readinggraph"
today = date.today()
formatted_today = today.strftime("%Y%m%d")

print(formatted_today)
todays_data = {
    "date" : formatted_today,
    "quantity" : "30"
}
# graph_posting_response = requests.post(url=f"{graph_endpoint}/{graphID}", json=todays_data, headers=header)
# print(graph_posting_response.text)

# Delete request
print(f"{graph_endpoint}/{graphID}/{formatted_today}")
delete_request = requests.delete(url=f"{graph_endpoint}/{graphID}/{formatted_today}", headers=header)
print(delete_request.text)