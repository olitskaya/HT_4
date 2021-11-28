# Написати функцію, яка приймає на вхід список і
# підраховує кількість однакових елементів у ньому.

def user_list(n):
    user_list_1 = []
    for i in range(n):
        print('Enter item ', i,  'of the list: ')
        x = input()
        user_list_1.append(x)
    print('User list: ', user_list_1)    
    return user_list_1    

def same(list_1):
    result = 0
    for i in list_1:
        k = list_1.count(i)
        if k > 2:
            result += 1
    print('The number of identical elements: ', result)        
    return result
    
number = int(input('Enter the number of list items: '))
test_list = user_list(number)  
same(test_list)
