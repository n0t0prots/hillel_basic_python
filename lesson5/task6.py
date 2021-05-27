def remove_empty_from_dict():
    dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
    dict_remove = {k: v for k, v in dict.items() if v is not None}
    print(dict_remove)


remove_empty_from_dict()
