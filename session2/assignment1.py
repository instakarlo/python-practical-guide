name = input('Enter name: ')
age = input('Enter age: ')


def get_decades(age):
    return int(age) // 10


def print_name_age(name, age):
    print(name + ' ' + age)


def print_two_data(data1='', data2=''):
    """ Prints two data into one string """
    print(data1 + ' ' + data2)


print_name_age(name, age)
print_two_data(name, age)

print('Decades for ' + age + ' is ' + str(get_decades(age)))
