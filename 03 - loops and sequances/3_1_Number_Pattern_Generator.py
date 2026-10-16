def number_pattern(n):
    number_list = []
    if not isinstance (n, int):
        return ('Argument must be an integer value.')
    elif n <= 0:
        return ('Argument must be an integer greater than 0.')
    else:
        number_list = list(range(1, n+1))
    return ' '.join(str(number_str) for number_str in number_list)
print (number_pattern(4))