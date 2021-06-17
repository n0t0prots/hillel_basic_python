import re


def password_check():
    your_password = input('Enter your password: ')
    requests = [['a-z'], ['A-Z'], ['0-9'], '[($)(@)(-)(+)(=)]']
    reply = 'Password is OK'
    i = 0
    while i < 4:
        if not re.search(rf"{requests[i]}", your_password):
            reply = []
            reply.append(f'not enough  {requests[i]} ')
        i += 1
    if len(your_password) < 8:
        reply.append('Too short password, 8 or more symbols needed ')
    print(reply)
    return reply



password_check()