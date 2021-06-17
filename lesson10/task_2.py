def check_if_palindrome():
    your_word = input()
    if your_word != your_word[::-1]: # -1 здесь шаг строки: от конца к началу
        print("It's not palindrome")
    else:
        print("It's palindrome")
input()


check_if_palindrome()
