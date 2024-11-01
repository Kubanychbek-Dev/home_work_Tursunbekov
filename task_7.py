# Напишите функцию, которая проверяет является ли число
# палиндромом. Число передаётся в качестве параметра. Если
# число палиндром нужно вернуть из функции true, иначе false.


def checking_number_for_palindrome(st):
    num = str(st)
    if num == num[::-1]:
        print("True")
    else:
        print("False")


def ask_num_for_check():
    try:
        ask_for_num = int(input("Введите число для проверки на палиндромом: "))
    except ValueError:
        print("Введите только целое число")
    else:
        checking_number_for_palindrome(ask_for_num)


ask_num_for_check()