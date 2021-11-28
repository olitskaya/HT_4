# Написати функцію, яка приймає на вхід список і
# підраховує список однакових елементів у ньому.

def user_list(n):
    user_list_1 = []
    for i in range(n):
        print('Enter item ', i,  'of the list: ')
        x = input()
        user_list_1.append(x)
    print('User list: ', user_list_1)    
    return user_list_1    

def same(list_1):
    elements = {i:list_1.count(i) for i in list_1}
    print('The number of identical elements: ', elements)        
    return elements
    
number = int(input('Enter the number of list items: '))
test_list = user_list(number)  
same(test_list)
