import os
import random
import subprocess
import time

# Specify the file name where you want to add the random code
file_name = "random_key_v2.cs"

# Function to create and add a random code to the file
def create_and_commit_random_code():
    # Generate a random code
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    # Use Git commands to stage and commit the changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-a", "-m", f"Added random code: {random_code}"])

# Number of commits to create
num_commits = 50000  # You can change this to the desired number

# Create and commit random code in a loop
for _ in range(num_commits):
    create_and_commit_random_code()
    # time.sleep(1)  # Sleep for 60 seconds before the next commit
