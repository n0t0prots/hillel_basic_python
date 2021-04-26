def spliter_str(func):
    def spliterr():
        str_1 = func().split()
        print(str_1)
    return spliterr


@spliter_str
def returner():
    str_2 = input('Enter your own string: ')
    print(str_2)
    return str_2


returner()


