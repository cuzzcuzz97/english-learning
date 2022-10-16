import os

import pathlib

dir_path = pathlib.Path().resolve()
list_vocab = f"{dir_path}/words_file"

with open('words_list.txt', 'w') as f:
    for file in os.listdir(list_vocab):
            if file.endswith(".txt"):
                list_file = os.path.join("", file)
                f.write(f"{list_file}\n")
                