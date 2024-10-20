# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все четные числа между ними


def even_nums():
    x = int(input("Enter start of range: "))
    y = int(input("Enter end of range: "))

    for i in range(x, y):
        if i % 2 == 0:
            print(i)


even_nums()