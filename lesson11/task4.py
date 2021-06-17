def fake_string(string, pat, rem_pat, times):
    string = string.replace(pat, rem_pat, times)
    return print(string)


fake_string('DC makes good movie', 'DC', 'Marvel', 1)