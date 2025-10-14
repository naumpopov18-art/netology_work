files = ['1.txt', '2.txt', '3.txt']
file_list = []

for name in files:
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_list.append((len(lines), name, lines))

file_list.sort()

with open('result.txt', 'w', encoding='utf-8') as result:
    for count, name, lines in file_list:
        result.write(f"{name}\n")
        result.write(f"{count}\n")
        result.writelines(lines)
        result.write("\n")