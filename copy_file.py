from return_data_file import data_file

def copy_str():
    data, nf_out = data_file(True)
    nf_in = 3 - nf_out
    count_rows = len(data)

    if count_rows == 0:
        print("Файл пустой из него нечего копировать")
    else:
        number_row = int(input(f"Введите номер строки которую нужно скопировать"
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        with open(f'db/data_{nf_in}.txt', 'a+', encoding='utf-8') as file:
            file.seek(0)
            file.write(';'.join([str((len(file.readlines()) + 1))] + data[number_row - 1].split(';')[1:]))
