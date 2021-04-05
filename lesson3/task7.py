factorial_number = int(input('Enter your number: '))
result = 1
for number in range(1, factorial_number+1):
    result = result * int(number)
print(result)
