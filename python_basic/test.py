'''import math
a=10
b=5
c=7
p=(a+b+c)/2

area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(area)
a = True
b = False
print(type(a)) 
z = None
print(z)
string = 'hello my name is Bekhzod'
print(len(string))
print(string.count('l'))
print(string.capitalize())
upper_cased = string.upper()
lower_cased = string.lower()
print(upper_cased.isupper())
print(lower_cased.islower())
print(string.islower())'''
empty_string = ''
if not empty_string:
    print('not empty')
else:
        print('empty')
h = 'hello'
print(h.startswith('hel'))
print(h.endswith('os'))

split = h.split('l')
print(type(split))
print(split)
split = h.split('e')
print(split)