import os
import random
import subprocess
import time

# Specify the file name where you want to add the random code
file_name = "random_key_v2.cs"

# Function to create and add a random code to the file and commit
def create_and_commit_random_code(commit_number, total_commits):
    # Generate a random code
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    # Use Git commands to stage and commit the changes
    subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "commit", "-m", f"Added random code: {random_code}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Calculate and display the progress as a percentage
    percentage = (commit_number / total_commits) * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')

# Number of commits to create
num_commits = 10000  # You can change this to the desired number

# Initialize the Git repository
subprocess.run(["git", "init"])

# Create and commit random code with progress
start_time = time.time()
for i in range(num_commits):
    create_and_commit_random_code(i + 1, num_commits)
end_time = time.time()

# Print final progress as 100%
print("Progress: 100.00% complete")

print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")
