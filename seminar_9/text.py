main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать файл',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']
main_menu_import_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu) - 1}: '

empty_book = 'Телефонная книга пуста или не открыта'
load_successful = 'Телефонная книга успешно загружена'
fields_new_contact = ['Введите имя контакта: ','Введите телефон: ','Введите комментарий: ']
input_search_word = 'Что будем искать: '
save_successful = 'Телефонная книга успешно сохранена'
input_del_uid = 'Введите ID контакта, который хотите удалить: '
fields_rename_contact = ['Введите новое имя контакта (Или Enter - без изменений): ',
                         'Введите новый телефон (Или Enter - без изменений): ',
                         'Введите новый комментарий (Или Enter - без изменений): ']
input_rename_uid = 'Введите ID контакта, который хотите изменить:'
goodbye = 'Программа завершена. До свидания!'

def contact_deleted(name: str) -> str:
    return f'Контакт {name} успешно удалён'

def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'


def empty_search(word: str) -> str:
    return f'Контакты, содержащие "{word}", не найдены'

def rename_successful(name: str) -> str:
    return f'Контакт {name} успешно изменён'