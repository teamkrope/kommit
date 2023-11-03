import os
import random
import subprocess
import time

file_name = "random_key.vue"

def create_and_commit_random_code(commit_number, total_commits):
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "commit", "-m", f"Added random code: {random_code}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    percentage = (commit_number / total_commits) * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')
    
num_commits = 75000
start_time = time.time()

for i in range(num_commits):
    create_and_commit_random_code(i + 1, num_commits)

end_time = time.time()

print("Progress: 100.00% complete")
print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")