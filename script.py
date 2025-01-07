import os
import subprocess

# initial run: git config --global --add safe.directory C:/folder-to-script.py
# and: git push --set-upstream origin main

# Path to the counter file
counter_file_path = 'counter.txt'

# Read the current counter value
if os.path.exists(counter_file_path):
    with open(counter_file_path, 'r') as file:
        content = file.read().strip()
        if content.isdigit():
            counter = int(content)
        else:
            counter = 0
else:
    counter = 0

# Increment the counter
counter += 1

# Write the new counter value back to the file
with open(counter_file_path, 'w') as file:
    file.write(str(counter))

# Add the file to the staging area
subprocess.run(['git', 'add', counter_file_path])

# Commit the change
commit_message = f'Update counter to {counter}'
subprocess.run(['git', 'commit', '-m', commit_message])

# Push the changes to the remote repository
subprocess.run(['git', 'push'])
