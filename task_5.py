# Напишите функцию, которая возвращает произведение чисел в
# указанном диапазоне. Границы диапазона передаются в
# качестве параметров. Если границы диапазона перепутаны
# (например, 5 - верхняя граница; 25 - нижняя граница), их нужно
# поменять местами.


class RangeError(Exception):
    pass


def product_of_nums(a, b):
    try:
        start = min(a, b)
        end = max(a, b)
        product = 1
        if a == b:
            raise RangeError("Границы диапазона одинаковые")
        elif a > b:
            print("Границы диапазона перепутаны, поэтому мы их поменяли местами.")
            print()
            for i in range(start, end + 1):
                product *= i
        else:
            for i in range(a, b + 1):
                product *= i
        print(f"Произведение чисел от {start} до {end} равно:\n{product}")
    except RangeError as err:
        print(err)


def get_ranges():
    try:
        start_of_range = int(input("Введите начало диапазона: "))
        end_of_range = int(input("Введите конец диапазона: "))
    except ValueError:
        print("Введите только целое число")
    else:
        product_of_nums(start_of_range, end_of_range)


get_ranges()