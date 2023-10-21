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

    # Get the current SHA of the file
    headers = {
        'Authorization': f'token {access_token}'
    }
    file_url = f'https://api.github.com/repos/{username}/{repository}/contents/random_key.txt'
    response = requests.get(file_url, headers=headers)
    current_file_info = response.json()
    current_sha = current_file_info['sha']

    # Create a new commit
    commit_message = f"Commit with random key: {random_key}"
    data = {
        'message': commit_message,
        'content': random_key,
        'branch': branch,
        'sha': current_sha  # Provide the current SHA
    }

    response = requests.put(file_url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

    if response.status_code == 200:
        print(f"Commit with random key {random_key} created successfully.")
    else:
        print(f"Failed to create commit: {response.status_code} - {response.text}")

while True:
    create_random_commit()
    time.sleep(50)  # Sleep for 5 seconds before the next commit
