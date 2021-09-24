greeting  = 'hello world'
chars = []
for l in greeting:
    chars.append(l)
print(chars)#bu yerda har bir hard alohida ' ' ichida joylashadi

#List comprehension  ni ishlatib listdagi harl larni bitta qoshtirnoq ichida yoza olamiza

chars = [l for l in greeting] #tepadagi code ni qisqart masi
chars = [ l for l in 'hello world'] #qilsak ham boladi

numbers = [n for n in range(6, 11)]
print(numbers)

'''num = [n*n for n in range(0,11)] #son kvadrati
print(num)'''

num = [n*n for n in range(15,25)if n%2 == 0]
print(num)

len_in_centimeters = [12,10,54,124,164]
#sm listidagi value larini ishlatib inches ga ozgartiramiza
len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeters]
print(f'inches: {len_in_inches} ')

chess_ratings = [2485, 2580, 2480, 2600, 2482, 2520]
titles = ['GM' if x>=2500 else 'MM' for x in chess_ratings]
print(titles) 

#juftlik ti topish Pairs

'''list1 = [2,4,-5,6,8-2]
list2 = [2,-6,8,3,5,-2]

pairs = []
for x in list1:
    for y in list2:
        current_sum = x + y
        if current_sum == 0:
            pairs.append((x,y))

print(pairs)'''

list1 = [2,4,-5,6,8-2]
list2 = [2,-6,8,3,5,-2]
pairs = [(x,y) for x in list1 for y in list2 if x+y == 0]