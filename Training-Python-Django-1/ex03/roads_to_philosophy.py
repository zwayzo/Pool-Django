import requests
import sys
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "MyWikiApp/1.0 (https://example.com; myemail@example.com)"
}

def save_to_file(filename, content):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n")

def first_link_outside_parentheses(paragraph):
    """
    Returns the first valid <a> link in a paragraph
    that is outside parentheses and not in italics.
    """
    parentheses_level = 0
    for elem in paragraph.descendants:
        if isinstance(elem, str):
            parentheses_level += elem.count("(")
            parentheses_level -= elem.count(")")
        elif elem.name == "a" and elem.get("href"):
            # Skip links in parentheses or in italics
            if parentheses_level == 0 and not elem["href"].startswith("#") and ":" not in elem["href"]:
                if not elem.find_parent(["i", "em"]):
                    return elem["href"]
    return None

def get_first_link(url, i):
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")

    # Print the main title
    title = soup.find("h1", {"id": "firstHeading"}).text
    
    
    # save_to_file("links.txt", title)

    content_div = soup.find("div", {"id": "mw-content-text"})
    paragraphs = content_div.find_all("p")
    
    for p in paragraphs:
        link = first_link_outside_parentheses(p)
        if link:
            print(title)
            return link
    
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python roads_to_philosophy.py <Wikipedia_Page_Name>")
        sys.exit(1)
    i = 1
    url = "https://en.wikipedia.org/wiki/" + sys.argv[1]
    visited = []

    try:
        while url != "https://en.wikipedia.org/wiki/Philosophy":
            if url in visited:
                print("It leads to an infinite loop!")
                break
            visited.append(url)
            next_link = get_first_link(url, i)
            i += 1
            if not next_link:
                print("It leads to a dead end!")
                sys.exit(1)
            url = "https://en.wikipedia.org" + next_link
            save_to_file("links.txt", url)
        print(f"{len(visited)} roads from {sys.argv[1]} to philosophy")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
