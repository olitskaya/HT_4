# Вводиться число. Якщо це число додатнє, знайти
# його квадрат, якщо від'ємне, збільшити його на
# 100, якщо дорівнює 0, не змінювати.

def number_change(number):
    result = 0
    if number > 0:
        result = number * number
    if number < 0:
        result = number + 100
    print('Result: ', result)

test_number = int(input('Enter a number: ')) 
number_change(test_number)
