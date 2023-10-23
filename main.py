import os
import random
import subprocess
import time
from multiprocessing import Pool

# Specify the file name where you want to add the random code
file_name = "random_key.go"

# Function to create and add a random code to the file and commit
def create_and_commit_random_code(_):
    # Generate a random code
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    # Use Git commands to stage and commit the changes
    subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "commit", "-m", f"Added random code: {random_code}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Number of commits to create
num_commits = 10

# Create and commit random code in parallel
if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=num_commits) as pool:
        pool.map(create_and_commit_random_code, range(num_commits))
    end_time = time.time()

    print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")
