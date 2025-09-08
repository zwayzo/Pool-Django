import sys

def ft_states(state_name):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    try:
        cap =  states.get(state_name.title())
        print(capital_cities[cap])
    except KeyError:
        print("Unknown state")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    ft_states(sys.argv[1])

    