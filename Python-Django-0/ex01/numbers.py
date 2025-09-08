def storage():
    tmp = ""
    with open("numbers.txt", "r") as file:
        for line in file:
            tmp += line.strip() 
    return tmp

def numbers():
    tmp = storage()
    out = ""
    for char in tmp:
        out += char
        if char == ',':
            print(out[:-1])
            out = ""

if __name__ == "__main__":
    numbers()