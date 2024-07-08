#filter_type
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(number_list):
    for number in number_list:
        number = number**2
        print(number)


def filter_numbers(list_for_filter, filter_type):
    if filter_type == 'odd':
        for number_type in list_for_filter:
            if number_type % 2 == 0:
                print(number_type)
    if filter_type == 'even':
        for number_type in list_for_filter:
            if number_type % 2 != 0:
                print(number_type)
    if filter_type == 'prime':
        for number_type in list_for_filter:
            if number_type <= 3:
                print(number_type)
            if number_type % 2 != 0:
                num = 3
                while num < number_type and number_type % num != 0:
                    num += 1
                    if num == number_type:
                        print(number_type)


def is_prime (list_for_prime, filter_type_for_prime):
    if filter_type_for_prime != 'prime':
        print('Эта функция только для определния простого числа из списка, измените значение парметра на prime')
    if filter_type_for_prime == 'prime':
        for number_type_prime in list_for_prime:
            if number_type_prime <= 3:
                print(number_type_prime)
            if number_type_prime % 2 != 0:
                num = 3
                while num < number_type_prime and number_type_prime % num != 0:
                    num += 1
                    if num == number_type_prime:
                        print(number_type_prime)


filter_numbers([1, 2, 3, 4, 25, 7, 19, 17, 101, 121, 199321, 9123], ODD)
filter_numbers([1, 2, 4, 6, 8, 9, 10], EVEN)
power_numbers([1, 2, 5, 7])
is_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], PRIME)