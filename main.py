import requests
import random
import time

# Replace with your GitHub access token and repository information
access_token = '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'
username = 'huzaifaasim017'
repository = 'test'
branch = 'master'

def create_random_commit():
    # Generate a random key for the commit message
    random_key = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Create a new commit
    commit_message = f"Commit with random key: {random_key}"
    data = {
        'message': commit_message,
        'content': random_key,
        'branch': branch,
    }

    headers = {
        'Authorization': f'token {access_token}'
    }

    response = requests.put(f'https://api.github.com/repos/{username}/{repository}/contents/random_key.txt', headers=headers, json=data)

    if response.status_code == 200:
        print(f"Commit with random key {random_key} created successfully.")
    else:
        print(f"Failed to create commit: {response.status_code} - {response.text}")

while True:
    create_random_commit()
    time.sleep(60)  # Sleep for 60 seconds before the next commit
