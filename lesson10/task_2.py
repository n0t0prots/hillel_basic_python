#def check_if_palindrome():
#    your_word = input()
 #   if your_word != your_word[::-1]: # -1 здесь шаг строки: от конца к началу
 #       print("It's not palindrome")
 #   else:
  #      print("It's palindrome")
# input()


# check_if_palindrome()
def check_if_palindrome():
    str = input("Enter the string: ")
    l = len(str)
    p = l-1
    index = 0
    while index < p:
        if str[index] == str[p]:
            index = index + 1
            p = p-1
        if index == p or index + 1 == p:
            print("String is a palindrome")
        else:
            print("string is not a palindrome")
        break

check_if_palindrome()