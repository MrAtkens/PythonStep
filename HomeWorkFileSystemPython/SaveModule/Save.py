import os

def save(value):
    path = input('Путь с файлом в который вы хотите сохранить: ')
    if os.path.exists(path):
        handle = open(path, "w")
        handle.write(str(value))
        handle.close()
        print('Операция успешно завершена \n')
    else:
        if os.path.isdir("Default"):
            filePath = f"{os.getcwd()}\\Default\\data.txt"
            handle = open(filePath, "w")
            handle.write(str(value))
            handle.close()
            print('Операция успешно завершена, данные сохранины в дефолтную папку рядом с данной программой \n')
        else:
            os.mkdir("Default")
            filePath = f"{os.getcwd()}\\Default\\data.txt"
            handle = open(filePath, "w")
            handle.write(str(value))
            handle.close()
            print('Операция успешно завершена, данные сохранины в дефолтную папку рядом с данной программой \n')
