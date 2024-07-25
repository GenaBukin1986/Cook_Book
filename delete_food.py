def delete_food():
    with open('./breakfast.txt','r',encoding='utf-8') as f:
        new_list = list(f)
        choice = input("\n\tВведите номер блюда, который вы хотите удалить: ")
        try:
            choice = int(choice)
            if 0 < choice < len(new_list) + 1:
                del new_list[choice - 1]
                print("\n\tБлюдо успешно удалено!")
                f_2 = open('./breakfast.txt','w',encoding='utf-8')
                for i in range(len(new_list)):
                    if i != len(new_list) - 1:
                        f_2.write(new_list[i])
                
                    else:
                        if new_list[i][:-1] == '\n':
                            f_2.write(new_list[i][:-1])
                        else:
                            f_2.write(new_list[i])
                input("\n\tНажмите Enter, чтобы продолжить ")
            else:
                print('\n\tВы ввели номер, которого нет!')
                input("\n\tНажмите Enter, чтобы продолжить ")
        except Exception:
            print("\n\tВы ввели не цифру!!!")
            input("\n\tНажмите Enter, чтобы продолжить ")