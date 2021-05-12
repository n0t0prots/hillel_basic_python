def func(l, n):
    return l[n:] + l[:n]
try:
    s=input('Введите список чисел через пробел: ')
    l = list(map(int, s.split()))
    if l == []:
        print('Пусто')
    else:
        a=input('Куда сдвиг?(Влево, вправо) - ')
        n = int(input('На сколько сдвиг? - '))
        while len(l)<n:
            n-=len(l)
        if a[1:5] == 'прав':
            print(func(l,-n))
        elif a[1:4] == 'лев':
            print(func(l,n))
        else:
            print('Вы не указали куда сдвинуть')
except:
    print('Что-то не так')


func(l, n)
