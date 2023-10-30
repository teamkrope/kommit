import random
import time
import git

file_name = "random_key_v3.r"

def create_and_commit_random_code(commit_number, total_commits):
    random_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

    # Write the random code to the file
    with open(file_name, "a") as file:
        file.write(f"Random Code: {random_code}\n")

    repo = git.Repo(search_parent_directories=True)
    repo.index.add([file_name])
    repo.index.commit(f"Added random code: {random_code}")

    percentage = (commit_number / total_commits) * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')

num_commits = 100
start_time = time.time()

for i in range(num_commits):
    create_and_commit_random_code(i + 1, num_commits)

end_time = time.time()

print("Progress: 100.00% complete")
print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")
