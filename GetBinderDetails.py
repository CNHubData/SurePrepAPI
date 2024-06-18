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

# GET BINDERS API

def getbinderdetails(Token, TaxYear, ClientID, BinderType):
    uri = "https://api.sureprep.com/V5.0/BinderInfo/GetBinderDetails"

    headers = {
        "Content-Type": "application/json",
        "AuthToken": Token
    }

    body = {
        "TaxYear": TaxYear,
        "ClientID": [ClientID],
        "BinderType": BinderType
    }

    response = requests.post(uri, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

TaxYear = 2023
ClientID = "20240800001"
BinderType = "1040"

try:
    binder = getbinderdetails(Token, TaxYear, ClientID, BinderType)
    print(f"Binder Details: {binder}")
except Exception as e:
    print(f"An error occurred while fetching binder details: {e}")
