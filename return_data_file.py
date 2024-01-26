from choice_file import choice_number_file


def data_file(copy_ = False):
    nf = choice_number_file(copy_)
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
