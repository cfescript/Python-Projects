import os



fPath = "E:\\Programming\\Python\\A\\"

dirContent = os.listdir(fPath)
absDir = []

for i in range(len(dirContent)):
    absDir.append(os.path.join(fPath, dirContent[i]))
    print("{} was created {} seconds ago".format(absDir[i], os.path.getmtime(absDir[i])))


'''
def writeData():
    data = "\nHello world!"
    with open("test.txt", 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()



if __name__ == "__main__":
    openFile()
    writeData()
    openFile()
'''
