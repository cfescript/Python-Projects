import sqlite3
import fnmatch

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

validFiles = []

for file in fileList:
    if fnmatch.fnmatch(file, '*.txt'): # Did a quick google search and this was the best I could do to compare two strings using a wild card. Is there a better way?
        validFiles.append(file)

conn = sqlite3.connect('validFiles.db')

with conn:
    cur = conn.cursor()
    cur.execute("\
        CREATE TABLE IF NOT EXISTS tbl_ValidFiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)\
        ")
    for file in validFiles:
        cur.execute("INSERT INTO tbl_ValidFiles(col_fname) VALUES (?)", ([file]))
    conn.commit()
conn.close()

validFileNames = ""

for file in validFiles:
    validFileNames += "\t{} \n".format(file)

print("Valid Files:\n{}".format(validFileNames))
        
