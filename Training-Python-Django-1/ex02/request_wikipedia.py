import requests
import dewiki
import sys

WIKI_API = "https://fr.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "MyWikiApp/1.0 (https://example.com; myemail@example.com)"
}

def search_wikipedia(query, lang="fr"):
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "search": query,
        "limit": 1,
        "namespace": 0,
        "format": "json"
    }
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    data = r.json()

    if len(data) > 1 and data[1]:
        return data[1][0]  # first suggestion
    return None

def get_wikipedia_page(title, lang="fr"):
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,
        "exintro": True,   # only intro
        "redirects": 1     # follow redirects
    }
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    data = r.json()

    page = next(iter(data["query"]["pages"].values()))
    text = page.get("extract", "")

    # Fallback: if no text, mark it
    if not text:
        return None

    cleaned = dewiki.from_string(text)
    save_to_file(title.replace(" ", "_"), cleaned)
    return cleaned



def wiki_lookup(query, lang="fr"):
    # Try direct fetch
    result = get_wikipedia_page(query, lang)
    if result:   # success with content
        return result

    # If empty or failed → search and fetch first result
    best_match = search_wikipedia(query, lang)
    # print("best_match:", best_match)
    if best_match:
        result = get_wikipedia_page(best_match, lang)
        if result:
            return result

    return f"No results found for '{query}'."


def save_to_file(filename, content):
    # print("content:", content)
    with open(filename + ".wiki", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    wiki_lookup(sys.argv[1], lang="fr")