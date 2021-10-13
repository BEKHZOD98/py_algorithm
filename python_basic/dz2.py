'''limit = int(input('enter the limit'))
total_sum = 0
for x in range(limit + 1):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x
    else: 
        continue
print(f'Total sum: {total_sum}')    

#problem solving with list comperhancion
limit = int(input('Enter your limit num: '))
tot_sum = sum([x for x in range(limit+1) if x %3 == 0 or x% 5==0 ])

print(f"sum limit nums:{tot_sum}") 

first_list = [1,2,3,4,5,6]
second_list = [11,12,13,14,15]

join_list = []
for x in first_list:
    if x % 2 != 0:
        join_list.append(x)
for x in second_list:
    if x % 2 == 0:
        join_list.append(x)

print(f'this is the new list: {join_list}')

#Merge list problem solved with list comperhancion
first_list = [1,2,3,4,5,6]
second_list = [11,12,13,14,15]

odds = [x for x in first_list if x % 2 !=0]
evens = [x for x in second_list if x % 2 ==0]

merge_list = odds + evens
print(f'Merged list: {merge_list}')'''

#problem black jack

cards = {
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7:0,
    8:0,
    9:0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1
}
current_hand = [2,3,4,10,'Q',5]

cards_sum = sum([cards[x] for x in current_hand ])
print(cards_sum)

