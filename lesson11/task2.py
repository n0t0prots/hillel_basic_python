def anonym_email():
    your_email = str(input('Enter your email: '))
    dog = your_email.index('@')
    new_email = your_email[:dog - 3] + '***@**' + your_email[dog + 3:]
    return new_email


print(anonym_email())


