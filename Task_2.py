# Написати функцію < bank >, яка працює за наступною логікою:
# користувач робить вклад у розмірі < a > одиниць строком на
# < years > років під < percents > відсотків (кожен рік сума
# вкладу збільшується на цей відсоток, ці гроші додаються до
# суми вкладу і в наступному році на них також нараховуються
# відсотки). Параметр < percents > є необов'язковим і має 
# значення по замовчуванню < 10 > (10%). Функція повинна
# принтануть і вернуть суму, яка буде на рахунку.

def bank(a, years, percents = 10):
    for i in range(years):
        a += a * (percents / 100)
    print('The amount on the account: ', a)
    return a
    
deposit_amount = int(input('Enter deposit amount: '))   
deposit_term = int(input('Enter deposit term: '))   
deposit_percentage = input('Enter deposit percentage: ')
if deposit_percentage == '':
    bank(deposit_amount, deposit_term)
else:
    bank(deposit_amount, deposit_term, float(deposit_percentage))
