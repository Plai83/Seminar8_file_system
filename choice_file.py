from print_data import print_file


def choice_number_file(copy_ = False):
    print_file()
    if copy_:
        number = int(input("Выберит файл, из которого копируем текст\n"
                           "Введите цифру 1 или 2: "))
    else:
        number = int(input("Выберит файл, с которым Вы хотите работать\n"
                           "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number
