# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно
# вернуть полученное количество цифр. Например, если
# передали 3456, количество цифр будет 4.


def number_of_digits_in_num(num):
    number_of_digits = 0
    for i in range(len(num)):
        if num[i].isdigit():
            number_of_digits += 1
    print(f"Количество цифр в числе {number_of_digits}")


ask_for_digit = input("Введите число: ")
number_of_digits_in_num(ask_for_digit)
