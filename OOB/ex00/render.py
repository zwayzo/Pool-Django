import os
import re
import sys

def parse():
    # print(len(sys.argv))
    if len(sys.argv) != 2:
        print("Usage: python render.py <input_file>")
        sys.exit(1)
    if os.path.splitext(sys.argv[1])[1] != ".template":
        print("Error: Input file must have a .template extension")
        sys.exit(1)
    try:
        with open("settings.py", 'r') as file:
            content = file.read()
            name = re.search(r'name\s*=\s*"([^"]+)"', content)

            print("content:", content)
        with open(sys.argv[1], 'r') as file:
            template = file.read()
            template = template.replace("{name}", name.group(1))
            print("template:", template)
        output_file = os.path.splitext(sys.argv[1])[0] + ".html"
        with open(output_file, 'w') as file:
            file.write(template)
            print(f"Output written to {output_file}")
    except FileNotFoundError:
        print("Error: settings.py file not found")
        sys.exit(1)

if __name__ == "__main__":
    parse() 