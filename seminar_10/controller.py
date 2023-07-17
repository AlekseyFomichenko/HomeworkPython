import view
import model
import text

main_phone_book = model.Phonebook()
def search_model():
    word = view.input_data(text.input_search_word)
    result = main_phone_book.search(word)
    view.show_contact(result, text.empty_search(word))

def start():
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                main_phone_book.open_file()
                view.print_msg(text.load_successful)
            case 2:
                main_phone_book.save_file()
                view.print_msg(text.save_successful)
            case 3:
                pb = main_phone_book.phone_book
                view.show_contact(pb, text.empty_book)
            case 4:
                contact = view.input_new_contact(text.fields_new_contact)
                main_phone_book.add_contact(contact)
                view.print_msg(text.new_contact_successful(contact[0]))
            case 5:
                search_model()
            case 6:
                search_model()
                uid = view.input_number(text.input_rename_uid)
                rename = view.input_new_contact(text.fields_rename_contact)
                name = main_phone_book.change_contact(uid, rename)
                view.print_msg(text.rename_successful(name))
            case 7:
                search_model()
                uid = view.input_number(text.input_del_uid)
                name = main_phone_book.delete_contact(uid)
                view.print_msg(text.contact_deleted(name))
            case 8:
                view.print_msg(text.goodbye)
                break