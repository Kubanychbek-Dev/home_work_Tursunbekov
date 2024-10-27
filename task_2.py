# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все четные числа между ними


def find_even_nums(x, y):
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i)


def get_ranges():
    try:
        x = int(input("Enter start of range: "))
        y = int(input("Enter end of range: "))
    except ValueError:
        print("Введите только целое число")
    else:
        find_even_nums(x, y)




get_ranges()