import os
import random
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

file_name = "random_key.py"

def create_and_commit_random_codes(commit_numbers, total_commits):
    for commit_number in commit_numbers:
        random_codes = [''.join(random.choice('0123456789ABCDEF') for _ in range(8)) for _ in range(commit_number)]
        with open(file_name, "a") as file:
            for code in random_codes:
                file.write(f"Random Code: {code}\n")

    subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "commit", "-m", f"Added {len(commit_numbers)} random codes"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

num_commits = 100000
batch_size = 1000
num_batches = num_commits // batch_size

start_time = time.time()

with ThreadPoolExecutor(max_workers=8) as executor:  # Adjust the number of workers as needed
    for i in range(num_batches):
        commit_numbers = [batch_size] * batch_size
        executor.submit(create_and_commit_random_codes, commit_numbers, num_commits)

end_time = time.time()

print(f"Total time taken for {num_commits} commits: {end_time - start_time:.2f} seconds")
