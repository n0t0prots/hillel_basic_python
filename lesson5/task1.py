num = int(input('Enter the number until 1000:'))


def is_prime():
    n = 2
    if num in (1, 2):
        res = 'Prime number'
    else:
        while n < num:
            if num % n != 0:
                res = 'Prime number'
            else:
                res = 'Not prime number'
                break
            n += 1
    print(res)


is_prime()
