import random

variants = ['yes', 'no', 'no']  # array for imitation doors and variants
CountOfCheck = 1000  # iteration Count for check result. If iteration count 10000 result = 60% or more then 60%


def checkWithoutChange(data):
    random.shuffle(data)
    return data[random.randrange(len(data))]


def checkWithChange(data):
    random.shuffle(data)
    secondChoiseVariant = 0
    firstChoiseVariant = random.randrange(len(data))
    for i in range(len(data)):
        if i != firstChoiseVariant and data[i] == 'no':
            secondChoiseVariant = i
            break
        for i in range(len(data)):
            if i != firstChoiseVariant and i != secondChoiseVariant:
                return data[i]


def checkTheory(iterationCount, array):
    winWithChange = 0
    winWithoutChange = 0
    for iterator in range(iterationCount):
        result = checkWithoutChange(array)
        if result == 'yes':
            winWithChange += 1

    for iterator in range(iterationCount):
        result = checkWithChange(array)
        if result == 'yes':
            winWithoutChange += 1

    if winWithChange / iterationCount > winWithoutChange / iterationCount:
        print('True its change strategy: ' + str((winWithChange / iterationCount) * 100) + '%')
    else:
        print('True its no change strategy: ' + str((winWithoutChange / iterationCount) * 100) + '%')


checkTheory(CountOfCheck, variants)  # True always change strategy