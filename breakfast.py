def list_breakfast():
    with open('./breakfast.txt','r',encoding='utf-8') as f:
        for index, value in enumerate(list(f),start=1):
            print(f'\t{index}. {value}',end='')

def add_list():
    with open('./breakfast.txt','a',encoding='utf-8') as f,\
        open('./breakfast.txt','r',encoding='utf-8') as f_2:
        name_food = input("\n\tВведите новое блюдо: ").capitalize()
        list_food = list(f_2)
        if name_food + '\n' in list_food or name_food in list_food:
            print("\n\tТакое блюдо уже есть в списке блюд!\
                \n\tПридумайте новое!")
        else:
            f.write('\n')
            f.write(name_food)
            print(f'\n\tБлюдо {name_food} успешно добавлено!')