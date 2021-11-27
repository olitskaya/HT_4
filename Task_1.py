# Написати функцію < square >, яка прийматиме один аргумент - 
# і вертатиме 3 значення (кортеж): периметр квадрата,
# площа квадрата та його діагональ.

def square(side):
    perimetr = 4 * side
    square = side * side
    diagonal = side * (2 ** (0.5))
    result = (perimetr, square, diagonal)
    print('Perimetr: ', result[0])
    print('Square: ', result[1])
    print('Diagonal: ', result[2])
    return result

a = int(input('Enter the side of the square: '))
square(a)
