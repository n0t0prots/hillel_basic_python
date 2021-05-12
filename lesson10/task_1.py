def create_your_file():
    your_file = input('Enter name of your file: ')
    f = open(your_file, 'w+')
    while True:
        create = input()
        if create == '':
           break
        f.write(create+'\n')
    f.close()



create_your_file()
