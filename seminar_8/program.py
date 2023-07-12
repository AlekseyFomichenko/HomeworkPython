book_dict = {}

def show_phonebook():
    with open('seminar_8\phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
    return data

def add_contact(name, number):
    with open('seminar_8\phonebook.txt', 'a', encoding='UTF-8') as file:
        book_dict[name] = number
        file.write('{}: {}\n'.format(name, number))
    return book_dict

def change_contact(name, new_name):
    with open('seminar_8\phonebook.txt', 'r', encoding='UTF-8') as file:
        for i in file.readlines():
            if i:
                key, value = i.strip().split(':')
                book_dict[key] = value
        for i in book_dict.keys():
            if i == name:
                book_dict.pop(i)
                with open('seminar_8\phonebook.txt', 'w', encoding='UTF-8') as file:
                    for key, value in book_dict.items():
                        file.write(f'{key}:{value}\n')
                i = new_name
                book_dict.update(i)
                with open('seminar_8\phonebook.txt', 'a', encoding='UTF-8') as file:
                    file.write('\n{}'.format(i))
                return i
            else:
                return 'Контакт не найден'    

def delete_contact(name):
    contact = ''
    with open('seminar_8\phonebook.txt', 'r', encoding='UTF-8') as file:
        for i in file.readlines():
            if i:
                key, value = i.strip().split(':')
                book_dict[key] = value
        for i in book_dict:
            if i == name:
                contact = i
                with open('seminar_8\phonebook.txt', 'w', encoding='UTF-8') as file:
                    book_dict.pop(contact)
                    for key, value in book_dict.items():
                        file.write(f'{key}:{value}\n')
                    return 'Контакт успешно удалён'
        return 'Контакт не найден'

def find_contact(name):
    with open('seminar_8\phonebook.txt', 'r', encoding='UTF-8') as file:
        for i in file.readlines():
            if i:
                key, value = i.strip().split(':')
                book_dict[key] = value
        for i in book_dict.keys():
            if i == name:
                return f'{i} - {book_dict[i]}'
        return 'Контакт не найден'

flage = True
while flage:
    print('''
    1 - добавить контакт
    2 - удалить контакт
    3 - найти контакт
    4 - показать контакты
    5 - изменить контакт
    6 - выйти''')
    answer = input('Выберите действие: ')
    if answer == '1':
        insert_name = input('Enter name contact: ')
        insert_number = input('Enter number contact: ')
        print(add_contact(name= insert_name, number= insert_number))
    if answer == '2':
        insert_name = input('Enter name contact: ')
        print(delete_contact(name=insert_name))
    if answer == '3':
        insert_name = input('Enter name contact: ')
        print(find_contact(name=insert_name))
    if answer == '4':
        print(show_phonebook())
    if answer == '5':
        insert_name = input('Enter name contact: ')
        insert_new_name = input('Enter name contact: ')
        print(change_contact(name= insert_name, new_name= insert_new_name))
    if answer == '6':
        print('Программа завершилась')
        flage = False