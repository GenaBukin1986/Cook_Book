from breakfast import list_breakfast, add_list
from menu import show_menu
from clear_display import clear_display
from delete_food import delete_food

if __name__ == '__main__':
    clear_display()
    print('\t=Программа \'Меню на неделю 1.0\'=\n')
    while True:        
        show_menu()
        choice = input("\n\tВведите пункт меню, который вы выбрали: ")
        if choice == '1':
            clear_display()
            print("\tСписок блюд: ")
            list_breakfast()
            input("\n\n\tДля продолжения нажмите Enter ")
            clear_display()
        if choice == '2':
            clear_display()
            add_list()
            input("\n\n\tДля продолжения нажмите Enter")
            clear_display()
        if choice == '3':
            clear_display()
            print("\tСписок блюд: ")
            list_breakfast()
            print()
            delete_food()
            clear_display()
        if choice == '4':
            break
    print("\n\tСпасибо, что выбрали нашу программу")