d = {
'Hendrix' : '1942',
'Allman' : '1946',
'King' : '1925',
'Clapton' : '1945',
'Johnson' : '1911',
'Berry' : '1926',
'Vaughan' : '1954',
'Cooder' : '1947',
'Page' : '1944',
'Richards' : '1943',
'Hammett' : '1962',
'Cobain' : '1967',
'Garcia' : '1942',
'Beck' : '1944',
'Santana' : '1947',
'Ramone' : '1948',
'White' : '1975',
'Frusciante': '1970',
'Thompson' : '1949',
'Burton' : '1939',
}

def alpha_sorted_items():
    sorted_by_key = dict(sorted(d.items(), key=lambda item: item[0]))
    for k, v in sorted_by_key.items():
        print(f"{k}")
        # print(f"{k}:{v}")

def year_sorted_items():
    sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
    for k, v in sorted_by_value.items():
        print(f"{k}")
        # print(f"{k}:{v}")

if __name__ == "__main__":
    print("Sorted by year:")
    year_sorted_items()
    print("\n\n\nSorted by name:")
    alpha_sorted_items()