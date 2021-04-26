def tmp_calculator(tmp_dgr, msr_dgr):
    tmp_k = 0
    tmp_c = 0
    tmp_f = 0
    if msr_dgr == 'C':
        tmp_c = tmp_dgr
        tmp_k = tmp_dgr + 273.15
        tmp_k = tmp_dgr * (5/9) + 32
    elif msr_dgr == 'k':
        tmp_k = tmp_dgr
        tmp_c = tmp_dgr - 273.15
        tmp_f = tmp_dgr * (5/9) - 459.7
    elif msr_dgr == 'F':
        tmp_f = tmp_dgr
        tmp_c = (tmp_dgr - 32) * (5/9)
        tmp_f = (tmp_dgr - 32) * (5/9) + 273.15
    else:
        print('This dimension does not exist.Try again!')
    return print('K = {:.2f} | C = {:.2f} | F = {:.2f}'.format(tmp_k, tmp_c, tmp_f))


temperature_degrees = float(input('Enter the temperature degree:'))
measuring_degrees = str(input('In which measuring is your temperature?(C, K, F) :'))

tmp_calculator(temperature_degrees, measuring_degrees)
