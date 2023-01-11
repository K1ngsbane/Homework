def txt_reader_1(file):
    my_file = open(file)
    result = my_file.read().split('\n')
    return result


def txt_reader_2(file):
    for elem in open(file, 'r'):
        yield elem.replace('\n', '')


my_list_1 = (txt_reader_1('data.txt'))
my_list_2 = list(txt_reader_2('data.txt'))
print(my_list_1)
print(my_list_2)
