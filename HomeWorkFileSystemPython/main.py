from GurpsConverterPackage.Length.Foot import *
from GurpsConverterPackage.Length.Metre import *
from GurpsConverterPackage.Length.Yard import *
from SaveModule.Save import save

isPause = True
while(isPause):
    print('1. Из фут в Метры \n',
    '2. Из Метры в футы \n',
    '3. Из Ярдов в метры \n',
    '4. Из Метров в Ярды \n',
    '5. Из Ярдов в футы \n',
    '6. Из Футов в ярды \n')
    operation = int(input('Выберите операцию: '))
    if isinstance(operation, int):
        if operation == 1:
            foot = int(input('Введите футы: '))
            if isinstance(foot, int):
                value = footToMetre(foot)
                print('Метры: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
        elif operation == 2:
            metre = int(input('Введите метры: '))
            if isinstance(metre, int):
                value = metreToFoot(metre)
                print('Футы: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
        elif operation == 3:
            yard = int(input('Введите ярды: '))
            if isinstance(yard, int):
                value = yardToMetre(yard)
                print('Метры: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
        elif operation == 4:
            yard = int(input('Введите метры: '))
            if isinstance(yard, int):
                value = metreToYard(yard)
                print('Ярды: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
        elif operation == 5:
            yard = int(input('Введите ярды: '))
            if isinstance(yard, int):
                value = yardToFoot(yard)
                print('Ярды: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
        elif operation == 6:
            foot = int(input('Введите футы: '))
            if isinstance(foot, int):
                value = footToYard(yard)
                print('Футы: ' + str(value))
                save(value)
            else:
                print('Не верный ввод')
    else:
        print('Не верный ввод')
            