def show_menu():
    print('\tМеню:')
    list_menu = [
        'Показать список блюд',\
            'Добавить блюдо',\
                'Удалить блюдо',\
                    'Выйти из программы']
    for index, value in enumerate(list_menu,start=1):
        print(f'\t{index}. {value}')