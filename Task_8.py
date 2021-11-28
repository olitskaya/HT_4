# Написати функцію, яка буде реалізовувати логіку циклічного зсуву
# елементів в списку. Тобто, функція приймає два аргументи: список
# і величину зсуву (якщо ця величина додатня - пересуваємо з кінця
# на початок, якщо від'ємна - навпаки - пересуваємо елементи з
# початку списку в його кінець).
# Наприклад:
# fnc([1, 2, 3, 4, 5], shift = 1) --> [5, 1, 2, 3, 4]
# fnc([1, 2, 3, 4, 5], shift = -2) --> [3, 4, 5, 1, 2]

def user_list(n):
    user_list_1 = []
    for i in range(n):
        print('Enter item ', i,  'of the list: ')
        x = input()
        user_list_1.append(x)
    print('User list: ', user_list_1)    
    return user_list_1    

def list_shift(user_list, shift):
    if shift < 0:
        shift = abs(shift)
        for i in range(shift):
            user_list.append(user_list.pop(0))
    else:
        for i in range(shift):
            user_list.insert(0, user_list.pop())
    print('New list: ', user_list)
    return user_list

number = int(input('Enter the number of list items: '))
test_list = user_list(number)      
test_shift = int(input('Enter the parametr of the shift: '))
list_shift(test_list, test_shift)
