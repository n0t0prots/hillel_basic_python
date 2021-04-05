import random
attempt = 3
while attempt:
    user_number = int(input('Enter your number: '))
    random_number = random.randint(0, 10)
    print(random_number)
    if user_number == random_number:
        print('You won')
        break
    else:
        print('You lose')
        attempt -= 1
