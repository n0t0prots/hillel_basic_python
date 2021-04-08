list_of_numbers = []
multiplexing = 1


def max_quantity(list_of_number):
    count = 0
    max_value = max(list_of_number)
    for i in list_of_numbers:
        if i == max_value:
            count += 1
    return count


def oddeven(list_of_numbers):
    even = 0
    odd = 0
    for i in list_of_numbers:
        if i % 2 == 0:
            even += 1
        if i % 2 != 0:
            odd += 1
    return odd, even


while True:
    input_data = int(input('Enter your number. Number 0 will finish the program: '))
    list_of_numbers.append(input_data)
    max_number = max(list_of_numbers)
    odd, even = oddeven(list_of_numbers)
    unique_list = list(set(list_of_numbers))
    unique_list.sort()
    unique_list.reverse()

    if input_data != 0:
        multiplexing = multiplexing * input_data
    if input_data == 0:
        print(f'Quantity of elements: {len(list_of_numbers)-1}')
        print(f'Sum of entered numbers: {sum(list_of_numbers)}')
        print(f'Product of numbers: {multiplexing}')
        print(f'Average value: {sum(list_of_numbers)/(len(list_of_numbers)-1)}')
        print(f'Max value in the list: {max_number}')
        print(f'Index number of max value: {list_of_numbers.index(max_number) + 1}')
        print(f'Odd numbers {odd}, even numbers {even}')
        print(f'Premax value: {unique_list[1]}')
        print(f'Quantity of max elements: {max_quantity(list_of_numbers)}')
        break