import json
import os
import requests

url = os.environ.get('GCLOUD_HTTP_RESOURCE', '')
metadata_server_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='
token_full_url = metadata_server_url + url
token_headers = {'Metadata-Flavor': 'Google'}
print("SENDING API CALL TO METADATA TO GET TOKEN")

token_response = requests.get(token_full_url, headers=token_headers)
jwt = token_response.text
print("GOT JWT RESPONSE")

# function_headers = {'Authorization': f'bearer {jwt}'}
# r = requests.get(url, headers=function_headers)
print("SETTING PAYLOAD")

json_data = {}
payload = json_data
headers = {
    'Authorization': f'bearer {jwt}',
    'Content-Type': 'application/json'
}
print("PAYLOAD: ", payload)

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
