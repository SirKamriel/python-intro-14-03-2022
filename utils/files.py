import os


def create_dir(dir_path, dir_name):
    os.makedirs(os.path.join(dir_path, dir_name))


def create_empty_file(dir_name, file_name):
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as txt_file:
        pass
