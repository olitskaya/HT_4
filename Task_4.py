# Написати функцію < prime_list >, яка прийматиме 2 аргументи - 
# початок і кінець діапазона, і вертатиме список простих чисел
# всередині цього діапазона.

def is_prime(number):
    result = True
    if number == 1:
        result = False
    else:          
        for i in range(2, number):
            if number % i == 0:
                result = False
                break
    return result

def prime_list(num_1, num_2):
    result_list = []
    for i in range(num_1, num_2):
        if is_prime(i):
            result_list.append(i)
    print('List of prime numbers in a given range: ', result_list)
    return result_list                
    
start_number = int(input('Enter a start number: '))   
finish_number = int(input('Enter a finish number: ')) 
prime_list(start_number, finish_number)
