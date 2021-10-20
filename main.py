import sqlite3
from os.path import exists

from classes.Person import Person


db_exists = exists('contacts.db')
con = sqlite3.connect('contacts.db')
cur = con.cursor()
if db_exists == False:
    cur.execute("CREATE TABLE contacts (name text, phone_number text, email text, address text)")
    cur.execute("INSERT INTO contacts VALUES ('João Miranda', '916660379', 'jomiranda710@gmail.com', 'Rua do Vale do Lobo, Montemor-o-Velho')")
    cur.execute("INSERT INTO contacts VALUES ('Miguel Torres', '9111111111', 'miki_torres@gmail.com', 'Rua, Santo Varão')")
    cur.execute("INSERT INTO contacts VALUES ('Lara Trindade', '912222222', 'lara_micaela_trindade2@gmail.com', 'Rua Carminé Miranda, Coimbra')")
    con.commit()


def show_contact_list():
    print('----------Contact List----------')

    # Print all contacts
    for row in cur.execute('SELECT * FROM contacts ORDER BY name'):
        print('Name:', row[0])
        print('Phone Number:', row[1])
        print('E-Mail:', row[2])
        print('Address:', row[3])
        print()
    print()
        

def add_contact():
    print('----------Add Contact----------')
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    email = input('E-Mail: ')
    address = input('Address: ')
    new_contact = Person(name, phone_number, email, address)
    cur.execute("INSERT INTO contacts VALUES (?, ?, ?, ?)", (new_contact.name, new_contact.phone_number, new_contact.email, new_contact.address))
    con.commit()

    print(name, 'added to contact list!\n\n')


def delete_contact():
    print('----------Delete Contact----------')
    contact = input('Which contact do you want to delete? ')

    cur.execute("SELECT * FROM contacts WHERE name = ?", (contact, ))
    data = cur.fetchall()
    if len(data) == 0:
        print('The contact you are trying to delete does not exist!\n\n')

    else:
        cur.execute("DELETE FROM contacts WHERE name = ?", (contact,))
        con.commit()
        print(contact, 'was deleted from contact list\n\n')


def unavailable_option():
    return 'Unavailable Option\n\n'


def menu():
    while 1:
        print('----------CONTACTS----------\n1 - Contact List\n2 - Add Contact\n3 - Delete Contact\n0 - Exit')
        # Menu option input
        option = eval(input())

        # Contact List
        if option == 1:
                show_contact_list()
            
        # Add Contact
        elif option == 2:
            add_contact()

        # Delete Contact
        elif option == 3:
            delete_contact()

        # Exit
        elif option == 0:
            print('Exiting...')
            break

        # Unavailable Option
        else:
            print(unavailable_option())


if __name__ == '__main__':
    menu()
    con.close()