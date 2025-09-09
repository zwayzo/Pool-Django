import sys

# states = {
#     "Oregon" : "OR",
#     "Alabama" : "AL",
#     "New Jersey": "NJ",
#     "Colorado" : "CO"
#     }
# capital_cities = {
#     "OR": "Salem",
#     "AL": "Montgomery",
#     "NJ": "Trenton",
#     "CO": "Denver"
# }
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
        print(capital_cities[cap], "is the capital of", state_name.title())
    except KeyError:
        print(state_name.title(), "is neither a capital city nor a state")


def ft_re_states(state_name):
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
        print(state_name, "is the capital of", reverse_states[cap])
    except KeyError:
        ft_states(state_name)

def output_all(args_list):
    for arg in args_list:
        ft_re_states(arg)


def args_clear(args_list):
    while '' in args_list:
        args_list.remove('')
    return  args_list

def args_parser(args):
    args_list = [item.strip() for item in args.split(',')]
    return args_clear(args_list)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit()
    print(args_parser(sys.argv[1]))
    output_all(args_parser(sys.argv[1]))
