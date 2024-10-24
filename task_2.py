# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все четные числа между ними


def even_nums():
    try:
        x = int(input("Enter start of range: "))
        y = int(input("Enter end of range: "))
    except ValueError:
        print("Введите только целое число")
    else:
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i)


even_nums()