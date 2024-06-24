import configparser
import requests
import os

# Authentication

def authenticate(UserName, Password, APIKey):
    uri = "https://api.sureprep.com/V5.0/Authenticate/GetToken"

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "UserName": UserName,
        "Password": Password,
        "APIKey": APIKey
    }

    response = requests.post(uri, headers=headers, json=body)
    print(f"Response Status Code: {response.status_code}")
    # print(f"Response Content: {response.text}")

    if response.status_code == 200:
        return response.json().get("Token")
    else:
        response.raise_for_status()

# Read credentials from sureprep.ini file

config = configparser.ConfigParser()
config.read('sureprep.ini')

# print("Current Working Directory:", os.getcwd())
# config_path = os.path.join(os.getcwd(), 'sureprep.ini')
# print("Expected config.ini path:", config_path)
# print("Does the config.ini exist at the expected path?", os.path.exists(config_path))

UserName = config['API']['UserName']
Password = config['API']['Password']
APIKey = config['API']['APIKey']

try:
    Token = authenticate(UserName, Password, APIKey)
    # print(f"Token: {Token}")
except Exception as e:
    print(f"An error occurred: {e}")

# CREATE BINDER API

unique_identifier = "fo8f4d60-d0de-4668-8ed5-6bd4a4bd534b"
email = "hharoldsen@coopernorman.com"
service_Type_ID = 0
template_ID = 0
office_Location_ID = 0
