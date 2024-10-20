# Напишите функцию, которая проверяет является ли число
# палиндромом. Число передаётся в качестве параметра. Если
# число палиндром нужно вернуть из функции true, иначе false.


def checking_number_for_palindrome(num):
    if num == num[::-1]:
        print("True")
    else:
        print("False")


ask_for_num = input("Введите число для проверки на палиндромом: ")
checking_number_for_palindrome(ask_for_num)