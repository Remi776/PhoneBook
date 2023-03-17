from model import add_contact as a
from model import convert_to as c
from model import interactions_with_contacts as iwc


def main_menu():
    flag = True
    while flag:
        answer = input('\nPhoneBook:\n'
                       '1. Display phone book\n'
                       '2. Add new contact\n'
                       '3. Search contact\n'
                       '4. Edit contact\n'
                       '5. Convert .json\n'
                       '6. Exit\n')
        match answer:
            case '1':
                try:
                    iwc.display_all_contacts()
                except FileNotFoundError:
                    print('Phone book is empty. Add contact.')
            case '2':
                a.add_contact()
            case '3':
                search_answer = input('\nSearch by:\n'
                                      '1.first_name\t2.last_name\t3.phone\t4.address\t5.email\t6.id\n')
                match search_answer:
                    case '1':
                        iwc.find_contact(0)
                    case '2':
                        iwc.find_contact(1)
                    case '3':
                        iwc.find_contact(2)
                    case '4':
                        iwc.find_contact(3)
                    case '5':
                        iwc.find_contact(4)
                    case '6':
                        iwc.find_contact(5)
                    case _:
                        print('There is no such option, try again.')
            case '4':
                edit_answer = input('\n1.Delete\n'
                                    '2.Rename\n')
                match edit_answer:
                    case '1':
                        iwc.display_all_contacts()
                        iwc.delete_contact()
                    case '2':
                        rename_answer = input('\nEdit:\n'
                                              '1.first_name\t2.last_name\t3.phone\t4.address\t5.email\t6.note\n')
                        match rename_answer:
                            case '1':
                                iwc.edit_contact(0)
                            case '2':
                                iwc.edit_contact(1)
                            case '3':
                                iwc.edit_contact(2)
                            case '4':
                                iwc.edit_contact(3)
                            case '5':
                                iwc.edit_contact(4)
                            case '6':
                                iwc.edit_contact(5)
                            case _:
                                print('There is no such option, try again.')
                    case _:
                        print('There is no such option, try again.')
            case '5':
                answer_convert = input('\nConvert .json to:\n'
                                       '1. .txt\t2. .csv\n')
                match answer_convert:
                    case '1':
                        c.convert_to_file()
                    case '2':
                        c.convert_to_csv()
            case '6':
                flag = False
            case _:
                print('Wrong number, try again.\n')


main_menu()
