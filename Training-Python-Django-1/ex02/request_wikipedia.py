import requests
import sys
import dewiki


def right_word(search):
    # print("welcome")
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search,
        "format": "json"
    }

    headers = {"User-Agent": "MyWikiApp/1.0 (https://example.com; myemail@example.com)"}

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    print("choose topic:")
    for result in data["query"]["search"]:
        print("-",result["title"])
    sys.exit()

def fetch_summary(title):
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }

    headers = {
        "User-Agent": "MyWikiApp/1.0 (https://example.com; myemail@example.com)"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    # print("data-->",data)
    i = 0
    try:
        pages = data["query"]["pages"]

        for page_id in pages:
            # print("hee\n")
            if "extract" in pages[page_id]:
                print("page:", pages[page_id]["extract"], ":", sys.getsizeof(pages[page_id]["extract"]))
                i += 1
            else:
                print("No extract found.")
                right_word(title)
        # sys.exit()
        # print("|||->",i)
        if i >= 1:
            sys.exit()
        else:
            right_word(title)
    except KeyError:
        print("No results found, please be more specific")
        right_word(sys.argv[1])
    # sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <search_term>")
        sys.exit(1)
    
    print("{}:",dewiki.from_string(sys.argv[1]))

    fetch_summary(dewiki.from_string(sys.argv[1]))
    print("No results found, please be more specific")
    # right_word(sys.argv[1])
