def anonym_email(email):
    dog = email.index('@')
    new_email = email[:dog - 3] + '***@**' + email[dog + 3:]
    return new_email


email = 'artemprocenko498@gmail.com'
print(anonym_email(email))