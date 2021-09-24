#while до техпор пока uzb 'qadar'
x = 0

while x < 3:
    print(f'x equals {x}') # bu code x 3ga teng bolishiga qadar ishlidi while qadar
    x+=1






#Shuning dek while bn if else ni ham ishlatsa boladi

num = 0
while num < 3:
    print(f'y equals {num}')
    num+=1
else: # y 3dan katta bop ketganida else ishlab ketadi
    print('Condition is not met',num)#shart bajarilmagan

vals = [1,2,3,4,5,6,7,8,9]
sum = 0

for v in vals:
    if v % 2 == 0:
        continue #agar shu line ga tushsa pasdagi code ishlamasdan keyingi index valuesiga utib ketadi
    else:
        sum+=v #sum har safargi valueni o'zida saqlidi
    if sum > 10: # qachongi shart true bolsa break boladi
        break 
print(sum)

for v in vals:
    pass # pass qilish

a = [ 10 ,3 ,3 ,45]
print(a)
a[1], a[3] = a[3], a[1]
print(a)

