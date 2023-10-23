import os
import random
import subprocess
import time

# Specify the file name where you want to add the random code
file_name = "random_key.go"

# Function to create and add a random code to the file
def create_random_code():
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

# Number of commits to create
num_commits = 10  # You can change this to the desired number

# Initialize the Git repository
# subprocess.run(["git", "init"])

# Perform batch commits
start_time = time.time()
for i in range(num_commits):
    create_random_code()

# Use Git commands to stage and commit all changes at once
subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.run(["git", "commit", "-m", f"Added {num_commits} random codes"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
end_time = time.time()

# Print the time taken
print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")
