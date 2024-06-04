import git
import os

file_name = "random_key.py"

# Create a repository if it doesn't exist
if not os.path.exists(".git"):
    repo = git.Repo.init()
else:
    repo = git.Repo()

# Create a new commit with an empty file
repo.index.commit("Initial commit")

# Create an empty file to serve as a reference
with open(file_name, "w") as file:
    file.write("")

# Define the total number of commits to make
total_commits = 300000

# Make 10,000 commits with minimal changes
for i in range(total_commits):
    with open(file_name, "a") as file:
        file.write("\n")
    
    repo.index.add([file_name])
    repo.index.commit(f"Commit {i + 1}")

    # Calculate and display the percentage completion
    percentage = (i + 1) / total_commits * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')

print(f"Created {total_commits} commits.")
