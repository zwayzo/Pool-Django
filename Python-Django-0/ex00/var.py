def my_var():
    number = 42
    print(number, " has type ", type(number))
    numstr = "42"
    print(numstr, " has type ", type(numstr))
    fr = "quarante-deux"
    print(fr, " has type ", type(fr))
    float_num = 42.0
    print(float_num, " has type ", type(float_num))
    a_bool = True
    print(a_bool, " has type ", type(a_bool))
    my_list = [42]
    print(my_list, " has type ", type(my_list))
    my_dict = {42: 42}
    print(my_dict, " has type ", type(my_dict))
    my_tuple = (42,)
    print(my_tuple, " has type ", type(my_tuple))
    my_set = set()   
    print(my_set, " has type ", type(my_set))


if __name__ == "__main__":
    my_var()