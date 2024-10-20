# Напишите функцию, которая возвращает минимальное из
# пяти чисел. Числа передаются в качестве параметров.


def find_min_num():
    min_num = []
    count = 1
    for i in range(1, 5 + 1):
        ask_nums = int(input(f"Enter {count} num: "))
        min_num.append(ask_nums)
        count += 1

    print("Минимальное число из пяти чисел:", min(min_num))


find_min_num()


# Простое решение

# def find_min_num(a, b, c, d, e):
#     lists = [a, b, c, d, e]
#     print("Минимальное число из пяти чисел:", min(lists))
#
#
# find_min_num(1, 2, 3, 4, 5)