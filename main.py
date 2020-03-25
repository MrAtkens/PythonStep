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

def loadDataToHtml(data):
    htmlStart = "<!DOCTYPE html><html lang=""en"" ><head> <meta charset=""UTF-8""> <title>Work</title> <link rel=""stylesheet"" href=""./style.css""></head><body><table class=""container""> <thead> <tr> <th>Id</th> <th>Full Name</th> <th>Position</th> <th>Login</th> <th>Password</th> </tr></thead> <tbody>"
    htmlTable = ""
    for stroke in data:
        htmlTable += f"<tr><td>{stroke['id']}</td><td>{stroke['fullName']}</td><td>{stroke['position']}</td><td>{stroke['login']}</td><td>{stroke['password']}</td></tr>"
    html = htmlStart + htmlTable + " </tbody> </table></body></html>"
    with open('index.html', 'w') as f:
        f.write(html)
        f.close()



data = getDataFromFile('data.txt')
loadDataToHtml(data)