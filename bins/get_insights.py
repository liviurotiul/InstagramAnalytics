import requests
import json

# Open the credentials json
CREDENTIALS_PATH = "/workspaces/socialFly/data/creds.json"

with open(CREDENTIALS_PATH) as json_file:
    credentials = json.load(json_file)

# Send request and get the response
endpointParams = {
    "input_token": credentials["access_token"],
    "access_token": credentials["access_token"]
}

url = credentials["graph_domain"] + "/debug_token"

response = requests.get(url, endpointParams)

print(response)