'''numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
hundred = range(1,100)
for i in hundred:
    print(i)

for i in range(1,4):
    print(i)
#odd and even num is in for loop
for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} is even number')
    else:
        print(f'{i} is odd number')
'''
num = [1,2,3,4,5]
for index, val in enumerate(num): #bu function dict , list , tuplening indexlarini numeratsiya qiladi
  #  num[index] *=2
    print(index, val)
print('***************************')
for index, val in enumerate(range(len(num))):
    print (index, val)
print("**********************")
tuple_fruits = ('banana','melon','apple')
for ind, val in enumerate(tuple_fruits,10):
    print(ind,val)
print("*******************")
name = 'Malik'
for l in name:
    print(l)
print('//////////////////')
for _ in range(5):
    print('Alert!')
print('--------------------')
person = ('Malik','silver',22)
for item  in person:
    print(item)