"""Способ, с помощью которого можно прочитать файл и изменить его"""
with open('./breakfast.txt','r',encoding='utf-8') as f:
    list_f = list(f)
    new_list = []
    for i in list_f:
        if i not in new_list and i+'\n' not in new_list:
            new_list.append(i)
    f_2 = open('./breakfast.txt','w',encoding='utf-8')
    for i in range(len(new_list)):
        if i != len(new_list) - 1:
            f_2.write(new_list[i])
        else:
            if new_list[i][:-1] == '\n':
                f_2.write(new_list[i][:-1])
            else:
                f_2.write(new_list[i])