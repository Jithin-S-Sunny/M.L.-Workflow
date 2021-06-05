import os
os.system('cmd /k "blastp -query example.txt -db sp -out output.txt"')
f=open('output.txt','r')
file_contents=f.read()
print(file_contents)

