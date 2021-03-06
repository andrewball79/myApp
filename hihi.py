import string
from functools import reduce
from time import time

from utility import performance

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
your_list = [9, 10, 11, 12, 13, 14, 15, 16]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# print(list(filter(check_odd, my_list)))
# print(list(map(multiply_by2, my_list)))
# print(list(map(lambda item: item * 2, my_list)))
# print(list(zip(my_list, your_list)))
# print(reduce(accumulator, my_list, 0))
# print(reduce(lambda acc, item: acc + item, my_list))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


# print(string.ascii_letters)
def to_capital(item):
    return item.upper()


# print(list(map(to_capital, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_numbers = [5, 4, 3, 2, 1]


def sort(item):
    return sorted(item)


# print(list(zip(sort(my_list), my_strings)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def check_pass(item):
    return item >= 50


# print(list(filter(check_pass, scores)))

# Lambda to the power of x
powers_list = [5, 4, 3]

# print(list(map(lambda num: pow(num, 2), powers_list)))

# list Sorting
az = [(0, 2), (4, 3), (9, 9), (10, -1)]
az.sort(key=lambda x: x[1])
# print(a)

# list, set, dictionary Comprehensions

my_comprehensive_list = [char for char in "hello"]
my_comprehensive_list2 = [num for num in range(0, 100)]
my_comprehensive_list3 = [num * 2 for num in range(0, 100)]
my_comprehensive_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
simple_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
my_dictionary = {key: value ** 2 for key, value in simple_dictionary.items() if value % 2 == 0}

my_dictionary2 = {my_pets[num - 1]: num for num in range(1, 5)}
# print(my_dictionary2)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))


# print(duplicates)


def my_decorator(func):
    def wrap_func(*x, **y):
        print('*****')
        func(*x, **y)
        print('*****')

    return wrap_func


@my_decorator
def hello(*args, emoji=":("):
    print(*args, emoji)


# hello("hi", ':(', 'chosen')


@performance
def long_time():
    for i in range(1):
        i * 5


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


# message_friends(user1)

# Error Handling

# while True:
#     try:
#         age = float(input('Enter your age '))
#         10/age
#     except ValueError:
#         print("Sorry please enter a number")
#         continue
#     except ZeroDivisionError:
#         print("Sorry, zero year olds can't play")
#         break
#     else:
#         print('Thanks!')
#         break
#     finally:
#         print('***')
#
# def sum_of_something(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'please enter numbers {err}')


# range(100)
# list(range(100))

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
#
# my_list80 = make_list(100)
# print(my_list80)


def fib(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


# f = fib(20)
# for x in f:
#     print(x)


def fib1(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b


# for x in fib1(20):
#     print(x)


print("Yes") if 5 > 2 else print("No")
