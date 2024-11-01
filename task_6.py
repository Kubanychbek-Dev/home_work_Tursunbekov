# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно
# вернуть полученное количество цифр. Например, если
# передали 3456, количество цифр будет 4.


def number_of_digits_in_num(num):
    into_str = str(num)
    number_of_digits = 0
    for i in range(len(into_str)):
        if into_str[i].isdigit():
            number_of_digits += 1
    print(f"Количество цифр в числе {number_of_digits}")



def get_num():
    try:
        ask_for_digit = int(input("Введите число: "))
    except ValueError:
        print("Введите только целое число")
    else:
        number_of_digits_in_num(ask_for_digit)


get_num()