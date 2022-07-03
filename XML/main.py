
import contextlib
from datetime import datetime,timedelta

path = r'C:\Users\kusib\OneDrive\Desktop\FTPprj-main\testpython - Copy.xml'
XMLPath = r'C:\Users\kusib\OneDrive\Desktop\FTPprj-main\XML.txt'
file_path = 'randomfile.txt'
f = open(r'C:\Users\kusib\OneDrive\Desktop\FTPprj-main\Rechnung - Kopie.txt')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
d = open(XMLPath)
d = d.read()

with open('filebeks.txt', 'w') as l:
    for y in Elemente:
        x = print(y, file=l)
nega = d.split('\n')
nega[3] = '<Pid>41010000001234567</Pid>'
print(nega)
