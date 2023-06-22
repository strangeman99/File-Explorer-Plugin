import requests
import json

# Define the API endpoint URL
url = 'http://127.0.0.1:8085/find-file'

# Set up the request payload
payload = {
    'name': 'fileToFind',
    'dirInfo': 'C:\\Users\\nicho\\OneDrive - The University of Western Ontario\\Side Projects'
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(f'Request failed with status code {response.status_code}')