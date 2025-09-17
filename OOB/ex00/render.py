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
    if os.path.exists(sys.argv[1]) is False:
        print(f"Error: {sys.argv[1]} file not found")
        sys.exit(1)
    try:
        with open("settings.py", 'r') as file:
            content = file.read()
            name = re.search(r'name\s*=\s*"([^"]+)"', content)
            # print("name:", re.search(r'surname\s*=\s*"([^"]+)"', content)[1])

            # print("content:", content)
        with open(sys.argv[1], 'r') as file:
            template = file.read()
            template = template.replace("{name}", name.group(1))
            template = template.replace("{surname}", re.search(r'surname\s*=\s*"([^"]+)"', content).group(1))
            template = template.replace("{age}", re.search(r'age\s*=\s*"([^"]+)"', content).group(1))
            template = template.replace("{profession}", re.search(r'profession\s*=\s*"([^"]+)"', content).group(1))
            print("template:",template)
            # print("template:", template)
        output_file = os.path.splitext(sys.argv[1])[0] + ".html"
        with open(output_file, 'w') as file:
            file.write(template)
            print(f"Output written to {output_file}")
    except FileNotFoundError:
        print("Error: settings.py file not found")
        sys.exit(1)

if __name__ == "__main__":
    parse()