
def power_numbers(number_list):
    for number in number_list:
        number = number**2
        print(number)


power_numbers([1, 2, 5, 7])


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


filter_numbers([1, 2, 3, 4, 25, 7, 19, 17, 101, 121, 199321, 9123], 'prime')
