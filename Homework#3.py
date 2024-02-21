import os
path = [text_name for text_name in os.listdir() if text_name[0].isdigit()]
def rewriting(path):
    data = {}
    for file_ in path:
        with open(file_, encoding='utf-8') as f:
            file_data = f.readlines()
            data[len(file_data)] = (file_, " ".join(file_data))

    data = dict(sorted(data.items()))
    with open('result.txt', 'w', encoding='utf-8' ) as new_f:
        for key, value in data.items():
            new_f.write(f'{value[0]} \n')
            new_f.write(f'{key} \n')
            new_f.write(f'{value[1]} \n')

rewriting(path)
