import os
dirpath = os.getcwd()

'''file=open('py_file.txt','w')as file:
    file.write('Name|phone
    
    ')'''
f = open("demo_pyfile.txt",'w')
f.write('1) I have deleted the content \n2) I have deleted the content ')
f.close()
f = open("demo_pyfile.txt","r")
datapy = f.read()
print('this is datapy: ',datapy)


#open , write and read second file
second_file=open('demo2_pyfile.txt','w')
second_file.write('1)Abbos\n2)Kabir\n3)Malik')
second_file.close()
second_file = open('demo2_pyfile.txt','r')
data = second_file.read()
print(data)

second_file = open('demo2_pyfile.txt','r')
data_sec_lines = second_file.readlines()
print(data_sec_lines)
second_file.close()
#open and read the file after the appending

f = open('demo_pyfile.txt','r')
#print(f.read())
'''
data = f.read()
f.seek(0)
print(data)'''
lines = f.readlines()
print(lines)
print(type(lines))
print(len(lines))


#delete folder or file
os.remove('demo2_pyfile.txt') 
#
print(second_file.closed)