n = int(input('Enter an integer: '))

if n % 2 == 0:
    if n > 20:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
else:
    print('Weird')


def swap_case(s):
    updated_string = ""
    for i in s:
        if i.islower():
            updated_string += i.upper()
        elif i.isupper():
            updated_string += i.lower()
        else:
            updated_string += i
    return updated_string