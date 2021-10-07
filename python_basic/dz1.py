'''row_num = int(input('enter your num: '))

for i in range(row_num):
      for i in range(i+1):
          print('*' ,end='')
      print('\n')

num = int(input('please enter num: '))

for i in range(0,num+1):
    #num+=1
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

rows = int(input('enter the number of rows'))
for x in range(rows):
    print('*'*(x+1))'''


'''num = int(input('enter the limit num: '))
#calc = [(sum(i) if i % 3 == 0 or i % 5 == 0 for i in num) ]

print('\n')
num_list = list(int(num) for num in input('enter the list items '))
sum_list = [(sum(num) if num % 3 == 0 or num % 5 == 0)]
print('user list: ',num_list)'''

'''first_lst = [1,2,3,4,5]
second_lst = [5,6,7,8,9]

# ваше решение ниже:
add_list = []
for item in range(0,len(first_lst)):
    if first_lst[item] % 2 == 0 or second_lst[item] % 3 == 0: 
        add_list.append(first_lst[item]+second_lst[item])
    else:
        continue
print(f'sum even and odd nums of list: {add_list}')
first_lst = [1,2,3,4]
second_lst = [5,6,7,8]
joined_list = []
for item in first_lst:
    if item % 2 !=0:
        joined_list.append(item)
for item in second_lst:
    if item % 2 == 0:
        joined_list.append(item)
print(f'added list: {joined_list}')'''






'''limit = int(input('enter the limit:'))
total_sum = 0
for x in range(limit+1):
    if x % 3 == 0 or x % 5==0:
        total_sum += x
print(f'Total sum = {total_sum}')
#list comperhancion

limit = int(input('Enter the comperhancion limit: '))
total_suml = sum([x for x in range(limit+1) if x % 3 == 0 or x % 5==0])
print(f'Comperhansion total sum: {total_suml}') 
'''

'''first_list = [1,2,3,4]
second_list = [5,6,7,8]
joined_list = []
for x in first_list:
    if(x % 2!=0):
        joined_list.append(x)
for x in second_list:
    if(x % 2 == 0):
        joined_list.append(x)

print(f'Merged list: {joined_list}')'''

first_list = [1,2,3,4]
second_list = [5,6,7,8]
joined_list = []
odd = [x for x in first_list if x % 2 !=0]
even = [x for x in second_list if x % 2 == 0]
'''joined_list.append(odd)
joined_list.append(even)'''
joined_list = odd + even

print(f'comperhancion list: {joined_list}')







      