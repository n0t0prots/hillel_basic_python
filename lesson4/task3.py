number_a = int(input('Enter your first number: '))
number_b = int(input('Enter your second number: '))
if number_a < number_b:
    for sequence in range(number_a, number_b+1):
        print(sequence)
else:
    for i in range(number_a, number_b-1, -1):
        print(i)
