num = [1,2,3,4,5]

'''for index in num:
    print(index)'''
'''
for i in range(50,60):
    if i % 2 == 0:
        print('even num: ',i)
    else:
        print('odd num: ', i)'''
'''for index , item in enumerate(num):
    print(num[index],item)'''
name = 'Habi'
for index in name:
    print(index)

for _ in range(3):
    print("Alarm!")
#for with tuple 
person = ('Holly',22,'sangmyung')
for item in person :
    print(item)

# List elon qilamiza va uni ichida tuple ni aniqlimiza
person1 = [('Habe',22,'sang'),('Malik',65,'myung')]
print(type(person1))
#person1 list ichidagi tuple ni index soni ni return qilamiza
print(len(person1))#bu yerda har bitta tuple alohida element dir











''' tuple unpacking '''
# !!! person1 list turida gi tuple ni loopda yugurib chiqamiza
for (name, age , univer) in person1 :
    print(f'{name} is {age} years old and studing in {univer}')



'''Dictionary with for loop'''
soccerPlayers = dict(Ronaldo = 37, Messi = 36, Neymar = 31)

for item in soccerPlayers:
    print(item)
#key and value ni con.log qilish
for item in soccerPlayers.items():
    print(item)

'''Unpacking'''
for k, v in soccerPlayers.items():
    print(f'{k} is {v} years old')

'''values() function'''
for value in soccerPlayers.values():
    print(value)










'''find all pairs sum of which equals zero'''
list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]

pairs = []
for x in list1: #설명 x1 = (y1,y2,y3,y4..) ,x2 = (y1,y2,y3,y4..),x3 = (y1,y2,y3,y4..)
    for y in list2: #shunday qilib x 2ga teng boganda y 6 marta o'z index lariga tenglash tirib chiqiladi
        current_sum = x + y
        if current_sum == 0:
            pairs.append((x,y))
print(pairs)















