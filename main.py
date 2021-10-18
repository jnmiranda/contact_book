from classes.Person import Person

def setup(contacts: list):
    joao = Person('João Miranda', '916660379', 'jomiranda710@gmail.com', 'Rua do Vale do Logo, Montemor-o-Velho')
    miguel = Person('Miguel Torres', '9111111111', 'miki_torres@gmail.com', 'Rua, Santo Varão')
    lara = Person('Lara Trindade', '912222222', 'lara_micaela_trindade2@gmail.com', 'Rua Carminé Miranda, Coimbra')

    contacts.append(joao)
    contacts.append(miguel)
    contacts.append(lara)


def show_contact_list(contacts: list):
    print('----------Contact List----------')
    for person in contacts:
        print('Name: ',person.name)
        print('Phone Number: ', person.phone_number)
        print('E-Mail: ', person.email)
        print('Address: ', person.address)
        print('\n')


def add_contact(contacts: list):
    print('----------Add Contact----------')
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    email = input('E-Mail: ')
    address = input('Address: ')
    new_contact = Person(name, phone_number, email, address)
    contacts.append(new_contact)
    print(name, 'added to contact list!\n\n')


def delete_contact(contacts: list):
    print('----------Delete Contact----------')
    contact = input('Which contact do you want to delete? ')
    for item in contacts:
        if contact == item.name:
            contacts.remove(item)
    print(contact, 'was deleted from contact list\n\n')


def unavailable_option():
    return 'Unavailable Option\n\n'


def menu(contacts: list):
    while 1:
        print('----------CONTACTS----------\n1 - Contact List\n2 - Add Contact\n3 - Delete Contact\n0 - Exit')
        # Menu option input
        option = eval(input())

        # Contact List
        if option == 1:
            show_contact_list(contacts)
            pass
            
        # Add Contact
        elif option == 2:
            add_contact(contacts)
            pass

        # Delete Contact
        elif option == 3:
            delete_contact(contacts)
            pass

        # Exit
        elif option == 0:
            print('Exiting...')
            break

        # Unavailable Option
        else:
            print(unavailable_option())




if __name__ == '__main__':
    contacts = []
    setup(contacts)
    menu(contacts)