import requests
import json

# Define the API endpoint URL
url = 'http://127.0.0.1:5000/find-file'

# Set up the request payload
payload = {
    'name': 'fileToFind',
    'dirInfo': ''
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Get the generated images from the response
    data = response.json()
    print(data)

else:
    print(f'Request failed with status code {response.status_code}')