import os
import requests

webhook_url = os.environ['DISCORD_WEBHOOK_URL']
file_path = 'test.pdf'

with open(file_path, 'rb') as f:
    payload = {
        'content': 'Here is the PDF file generated from test.md',
        'filename': 'test.pdf'
    }
    files = {
        'file': ('test.pdf', f)
    }
    response = requests.post(webhook_url, data=payload, files=files)

if response.status_code == 204:
    print("Successfully uploaded file to Discord.")
else:
    print(f"Failed to upload file to Discord. Status code: {response.status_code}")
    print(response.text)
