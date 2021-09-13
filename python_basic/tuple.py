strings = ('str1','str2','str3')#tuple bu constanta listi
print(type(strings))
print(strings[0])
len(strings)
strings.count('str1')

students = [('Malik',1999,'1kurs'),('Ali',2000,'2kurs'),('Abbos',1998,'3kurs')]
#students[0] = ('Abdu',1778,'0')
print(students)
print(type(students))

from collections import namedtuple
Students = namedtuple('Students','name age cours')
students = [Students('Malik',1999,'1kurs'),Students('Ali',2000,'2kurs'),('Abbos',1998,'3kurs')]
print(students[0].age)
