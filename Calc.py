import operator
from functools import reduce
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning(('Aktualny czas'))
print()
print()

# Dodawanie
def add(numbers):
    return reduce(operator.add, numbers)


# Odejmowanie


def subtract(numbers):
    return reduce(operator.sub, numbers)


# Mnożenie


def multiply(numbers):
    return reduce(operator.mul, numbers)


# Dzielenie


def divide(numbers):
    return reduce(operator.truediv, numbers)


def get_data():
    choice = input("Wybierz działanie(1/2/3/4): ")
    args = []
    if choice in "1234":
        while True:
            num = input("Podaj kolejną liczbę lub naciśnij q aby wyjść: ")
            if num == 'q':
                break
            args.append(float(num))
    return args, choice


print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
}

numbers, choice = get_data()
result = operations[choice](numbers)
print(result)
