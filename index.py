import re
import random
import string


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getDataFromFile(fileName):
    mainData = []
    with open('data.txt', 'r') as f:
        fileData = f.read().splitlines()
    for stroke in fileData:
        result = re.split(r':', stroke)
        dataSchema = {
            'id': 0,
            'fullName': '',
            'position': '',
            'login': '',
            'password': ''
        }
        dataSchema['id'] = result[0]
        dataSchema['fullName'] = result[1][:1] + '.' + result[2][:1] + ' ' + result[3]
        dataSchema['position'] = result[4]
        dataSchema['login'] = randomString(6)
        dataSchema['password'] = randomString(8)
        mainData.append(dataSchema)
    return mainData


data = getDataFromFile('data.txt')
print('FullName..............Id..............Position.............Login............Password\n')
for stroke in data:
    print(stroke['fullName'] + '           ' + stroke['id'] + '             ' + stroke['position'] + '               ' +
          stroke['login'] + '              ' + stroke['password'])
