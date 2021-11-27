# Написати функцію < fibonacci >, яка приймає один аргумент 
# і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(number):
    list_fibonacci = [1, 1, ]
    for i in range(2, number):
        number_fibonacci = list_fibonacci[i-2] + list_fibonacci[i-1]
        if number_fibonacci <= number:
            list_fibonacci.append(number_fibonacci)
        else:
            break
    print('A list of Fibonacci numbers that do not exceed a given: ', list_fibonacci) 
    return list_fibonacci

max_number = int(input('Enter number: '))
fibonacci(max_number)
