def work_with_list():
    s = []
    n = int(input())
    s.append(n)
    while n != 0:
        n = int(input())
        s.append(n)
    return s[:-1]


working_list = work_with_list()


def get_len_of_list(working_list):
    print(f'Count: {len(working_list)}')


get_len_of_list(working_list)


def sum_of_list(working_list):
    print(f'Sum all numb: {sum(working_list)}')


sum_of_list(working_list)


def multiply_list(working_list):
    m = 1
    for i in working_list:
        m *= i
    print(f'Composition: {m}')


multiply_list(working_list)


def average_of_list(working_list):
    print(f'AVG: {sum(working_list) // len(working_list)}')


average_of_list(working_list)


def max_of_list(working_list):
    print(f'Position of the maximum value in the list: {working_list.index(max(working_list)) + 1}')
    print(f'Maximum value in the list: {max(working_list)}')


max_of_list(working_list)


def chet_nechet_of_list(working_list):
    chet = 0
    nechet = 0
    for i in working_list:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1
    print(f'Even: {chet}, odd: {nechet}')


chet_nechet_of_list(working_list)


def sec_max_num(working_list):
    copy_of_list = list(set(working_list))
    for i in copy_of_list:
        if i == max(copy_of_list):
            del copy_of_list[copy_of_list.index(i)]
    print(f'Second largest number: {max(copy_of_list)}')


sec_max_num(working_list)


def count_of_max(working_list):
    count = 0
    m = max(working_list)
    for i in working_list:
        if i == m:
            count += 1
    print(f'Maximum numbers: {count}')


count_of_max(working_list)