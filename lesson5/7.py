from datetime import date


def foo(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False


print(foo(2021, 2, 28))
print(foo(2021, 2, 29))
