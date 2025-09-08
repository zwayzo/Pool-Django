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
    reverse_capital = {v: k for k, v in capital_cities.items()}
    reverse_states = {v: k for k, v in states.items()}
    try:
        cap =  reverse_capital.get(state_name.title())
        print(reverse_states[cap])
        # print(capital_cities[cap])
    except KeyError:
        print("Unknown state")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    ft_states(sys.argv[1])

    