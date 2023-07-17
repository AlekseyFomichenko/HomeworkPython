

class Phonebook:
    def __init__(self, path: str = 'seminar_10\phonebook.txt'):
        self.phone_book = {}
        self.path = path
        
    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            uid, name, phone, comment = contact.strip().split(';')
            self.phone_book[int(uid)] = [name, phone, comment]

    def add_contact(self, new: list[str]) -> str:
        uid = max(self.phone_book) + 1
        self.phone_book[uid] = new

    def search(self, word):
        result = {}
        for uid, contact in self.phone_book.items():
            for field in contact:
                if word.lower() in field.lower():
                    result[uid] = contact
                    break
        return result

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            all_contacts = []
            for uid, contact in self.phone_book.items():
                all_contacts.append(';'.join([str(uid), contact[0], contact[1], contact[2]]))
            all_contacts = '\n'.join(all_contacts)
            file.write(all_contacts)

    def delete_contact(self, uid: int)-> str:
        return self.phone_book.pop(uid)[0]

    def change_contact(self, uid: int, rename: list[str]):
        contact = self.phone_book.get(uid)
        for i in range(3):
            if rename[i]:
                contact[i] = rename[i]
        self.phone_book[uid] = contact
        return contact[0]