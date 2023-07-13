import requests

hec_url = 'https://52.174.22.39:8088/services/collector/event'
hec_token = 'abcd1234'

headers = {
    'Authorization': f'Splunk {hec_token}' ,
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = '{"event": "hello world"}'

response = requests.post(hec_url, headers=headers, data=data, verify=False)
print(response)