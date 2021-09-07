import os
dirpath = os.getcwd()

'''file=open('py_file.txt','w')as file:
    file.write('Name|phone
    
    ')'''
f = open("demo_pyfile.txt",'w')
f.write('1) I have deleted the content \n2) I have deleted the content ')
f.close()

#open and read the file after the appending
f = open('demo_pyfile.txt','r')
#print(f.read())
data = f.read()
f.seek(0)
print(data)
lines = f.readlines()
print(lines)
print(type(lines))