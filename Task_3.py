# Написати функцію < is_prime >, яка прийматиме 1 аргумент - 
# число від 0 до 1000, і яка вертатиме True, якщо це число
# просте, і False - якщо ні.

def is_prime(number):
    result = True
    if number == 1:
        result = False
    else:          
        for i in range(2, number):
            if number % i == 0:
                result = False
                break
    if result == True:
        print(number, 'is a prime number.')
    else:
        print(number, 'is not a prime number.')
    return result
    
test_number = int(input('Enter an integer from 0 to 1000: '))   
is_prime(test_number)
