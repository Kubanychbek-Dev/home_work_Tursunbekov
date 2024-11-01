# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
#  Bill Gates


with open("Gate's-text.txt", "rt", encoding="utf-8") as file:
    data = file.readlines()
    print(" ".join(data))