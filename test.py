s = []

with open('words_list.txt', 'r') as file:
    n = file.readlines()
    for w in n:
        w = w.replace('\n','')
        s.append(w)
print(s)        