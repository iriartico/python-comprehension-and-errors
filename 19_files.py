# with open('./info.txt', 'r+') as file:  # Escribe sobre un archivo
with open('./info.txt', 'w+') as file:  # Sobreescribe todo el archivo
    for line in file:
        print(line)
    file.write('\nadd some lines')
    file.write('\nadd some lines')
    file.write('\nadd some lines')
    file.write('\nadd some lines')
