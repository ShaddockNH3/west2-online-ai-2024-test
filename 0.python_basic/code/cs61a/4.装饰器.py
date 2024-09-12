def dec_fun(func):
    def wrapper_fun():
        print("one_plus_one")
        func()
        print("equel to 2")
    return wrapper_fun


@dec_fun
def one_plus_one():
    print (1+1)

one_plus_one()