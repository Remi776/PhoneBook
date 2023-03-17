import json


def display_all_contacts():
    data = json.load(open(file_base + files[0], encoding='utf-8'))
    for person in data:
        print(*person.values())


def find_contact(number):
    options_list = ['first_name', 'last_name', 'phone', 'address', 'email', 'id']
    search_list = list()
    user_answer = input(f'Enter the {options_list[number]}: ').lower()
    data = json.load(open(file_base + files[0], encoding='utf-8'))
    if number == 5:
        try:
            print(*data[int(user_answer)].values())
        except IndexError:
            print('Index does not exist. Try again.')
    else:
        for person in data:
            if person[options_list[number]].lower() == user_answer:
                search_list.append(person.values())
        if len(search_list) == 0:
            print(f'{options_list[number]}: {user_answer} does not exist. Try again.')
        else:
            for i in search_list:
                print(*i, end='\n')


def edit_contact(number):
    options_list = ['first_name', 'last_name', 'phone', 'address', 'email', 'note']
    user_id = int(input('\nEnter [id] of contact you want to edit: '))
    data = json.load(open(file_base + files[0], encoding='utf-8'))

    try:
        print(*data[user_id].values())
    except IndexError:
        print('Index does not exist. Try again.')
    data[user_id][options_list[number]] = input(f'Enter the new {options_list[number]}: ')
    print(*data[user_id].values())
    with open(file_base + files[0], 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'{options_list[number]} edited successfully.')


def delete_contact():
    user_id = int(input('\nEnter [id] of contact you want to DELETE: '))
    data = json.load(open(file_base + files[0], encoding='utf-8'))
    del data[user_id]
    with open(file_base + files[0], 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Contact successfully deleted.')
