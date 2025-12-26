# TASK 4 - Automation (File Renaming)

import os

folder = "test_files"

# create folder if not exists
if not os.path.exists(folder):
    os.mkdir(folder)

# create demo files
for i in range(1, 4):
    with open(f"{folder}/old{i}.txt", "w") as f:
        f.write("CodeAlpha")

files = os.listdir(folder)
count = 1

for file in files:
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, f"file_{count}.txt")
    os.rename(old_path, new_path)
    count += 1

print("Automation completed successfully!")