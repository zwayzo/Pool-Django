#  It must create a folder and a file inside this folder,
# write something in this file and
# then read and display its conte

from local_lib.path import Path

# Create a Path object for a file inside a folder
file_path = Path("test_folder/test_file.txt")

# Create necessary directories
file_path.parent.mkdir_p()

# Write content to the file
file_path.write_text("This is the test data.")

print(f"File '{file_path}' created successfully.")