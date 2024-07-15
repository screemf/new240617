#filter_type
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(number_list):
    new_list_sqr = []
    for number in number_list:
            new_value = number**2
            new_list_sqr.append(new_value)
    return new_list_sqr


def filter_numbers(list_for_filter, filter_type):
    filtered_num=[]
    if filter_type == 'odd':
        for number_type in list_for_filter:
            if number_type % 2 == 0:
                filtered_num.append(number_type)
        return filtered_num
    elif filter_type == 'even':
        for number_type in list_for_filter:
            if number_type % 2 != 0:
                filtered_num.append(number_type)
        return filtered_num
    if filter_type == 'prime':
        for number_type in list_for_filter:
            if number_type <= 3:
                filtered_num.append(number_type)
            elif number_type % 2 != 0:
                num = 3
                while num < number_type and number_type % num != 0:
                    num += 1
                    if num == number_type:
                        filtered_num.append(number_type)
        return filtered_num


def is_prime (list_for_prime, filter_type_for_prime):
    prime_num=[]
    if filter_type_for_prime != 'prime':
        print('Эта функция только для определния простого числа из списка, измените значение парметра на prime')
    elif filter_type_for_prime == 'prime':
        for number_type in list_for_prime:
            if number_type <= 3:
                prime_num.append(number_type)
            elif number_type % 2 != 0:
                num = 3
                while num < number_type and number_type % num != 0:
                    num += 1
                    if num == number_type:
                        prime_num.append(number_type)
        return prime_num


print(power_numbers([2, 3, 4, 5, 6, 7, 8, 9]))
print(filter_numbers([1,2,3,4,5,6,7],ODD))
print(filter_numbers([1,2,3,4,5,6,7],EVEN))
print(filter_numbers([1,2,3,4,5,6,7],PRIME))
print(is_prime([1,2,3,4,5,6,7,8,9],PRIME))
print(filter_numbers(power_numbers([1,2,3,4,5,6,7,8]),ODD))