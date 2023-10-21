import os
import random
import subprocess
import time

# Specify the file name where you want to add the random code
file_name = "random_key.cs"

# Specify your repository and branch information
repository = "test"
branch = "master"
new_branch = "develop_v1"  # Change this to the name of the new branch

# Function to create and commit random code to a specific branch
def create_commit_and_pull_request():
    # Generate a random code
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    # Use Git commands to stage and commit the changes to the new branch
    subprocess.run(["git", "checkout", "-b", new_branch])  # Create and switch to the new branch
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-a", "-m", f"Added random code: {random_code}"])

    # Push the new branch to the repository
    subprocess.run(["git", "push", "origin", new_branch])

    # Create a pull request from the new branch to the original branch
    subprocess.run(["hub", "pull-request", "-b", f"{repository}:{branch}", "-h", f"{repository}:{new_branch}"])

# Number of pull requests to create
num_pull_requests = 10  # You can change this to the desired number

# Create commits, branches, and pull requests in a loop
for _ in range(num_pull_requests):
    create_commit_and_pull_request()
    # Sleep for a few seconds to allow the pull request to be created
    time.sleep(10)
