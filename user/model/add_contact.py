import json

last_user_id = 0
files = ['.json', '.csv', '.txt']
file_base = 'phonebook'


def gen_contact():
    global last_user_id
    name, surname, phone, email, address, note = input('name: '), input('surname: '), \
                                                 input('phone: '), input('email: '), \
                                                 input('address: '), input('note: ')

    contact_template = {
        'id': last_user_id,
        'first_name': name,
        'last_name': surname,
        'phone': phone,
        'email': email,
        'address': address,
        'note': note
    }
    return contact_template


def add_contact():
    global last_user_id

    try:
        data = json.load(open(file_base + files[0]))
        last_user_id = data[-1]['id'] + 1
    except:
        data = []
    person_dict = gen_contact()
    data.append(person_dict)
    with open(file_base + files[0], 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
