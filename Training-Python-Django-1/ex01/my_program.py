from path import Path

# Create a Path object for current folder
p = Path(".")

# Print all files in the folder
for f in p.files():
    print(f)
