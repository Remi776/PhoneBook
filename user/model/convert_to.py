def convert_to_csv():
    data = json.load(open(file_base + files[0], encoding='utf-8'))
    columns = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'note']
    with open(file_base + files[1], 'w', encoding='utf-8') as file:
        wr = csv.DictWriter(file, fieldnames=columns)
        wr.writeheader()
        wr.writerows(data)
    print('File was successfully converted.')


def convert_to_file():
    data = json.load(open(file_base + files[0], encoding='utf-8'))
    with open(file_base + files[2], 'w', encoding='utf-8') as file:
        for person in data:
            for key, value in person.items():
                file.write(f'{value}\t')
            file.write('\n')
        file.close()
    print('File was successfully converted.')
