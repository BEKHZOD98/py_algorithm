players = {
    'Carlsen' : 2842,
    'Caruana' : 2822,
    'Mamedyarov' : 2801,
    'Ding' : 2797,
    'Giri' : 2780
        }
players = dict(Carlsen=2842, Caruana = 2822, Mamedyarov = 2801, Ding = 2797, Giri = 2780)
print(players)  
'''Carlsen bu dictionary ni 'key' dir score si esa uni 'znacheniyasi value' dir
   Dicrionary ni listda farqi ular listdan kora ancha tezroq ishlidi qachonki katta 
   data larni saqlab ularni 'key' orqali qidirilganida listdan kora tezroq ishlidi'''  
#endi esa dict ni keyga qarab console ga chiqarib koramiza
top1 = players['Carlsen']
print('Top chess player is: ',top1) #agarda bu usulda yozilsa consolega Carlsenni faqat value score chiqadi
      #qosh tirnoni ichida {top1} qilib ham yozsa boladi
#Bunda tashqari consolega chiqarishni 2chi yoli get() functionidan foydalanish dir
print(players.get('Ding'))
players['So'] = 2760 #qilib dictga yana bitta key va value ni qosha olamiza
print(players)
players.pop('Giri') # shu usulda girini delete qilamiza
#popitem orqali dict ni oxirgi key ini delete qilaolamiza
del players['So'] #orqali delete qisa boladi
print(players)
sorted()



#The method update() adds dictionary dict2's key-values pairs in to dict. 
student = {
    'Name': 'Habe', 'Age': 7
    }
Human = {
    'Sex': 'Male'
}
student.update(Human)
print(student)

#Dict ni faqat gina Key larini con.log qilish un keys() func ni ishlatamiza
keys = players.keys()
print(type(keys),keys)



#Dict ni key larini list functioniga solgan holda chiqarish ham qulay
lis = list(players.keys())
print(type(lis),lis) #Bunday holda lis variable type list boladi

#sorted
print(sorted(players.keys())) #abcd sort
#Agarda dict da "Keyga " o'xshagan key borligini tekshirish un in yoki not in ishlatiladi
print('Carlsen' in players)
print('Malik' not in players)

#Endi esa Dict ni faqatgina value sini con.log qilish
vals = players.values()
print(type(vals),vals)
#Va value ni listga solib con.log qilish
lis_dict_value = list(players.values())
print(type(lis_dict_value),lis_dict_value)
#Sorted functioni bn value ni ham sort qilamiza
print(sorted(players.values()))# 1->100
#Copy qilish
players_copy = players.copy()
print(players_copy)
players.pop('Ding')
print(players)
print(players_copy)#dictni copy qilinganda faqat gina ustki qismdan copy qilinadi memoryda saqlanadigan addresdan copy olinmidi va value ham ozgarmidi
                   #list da esa dict dan farqli olaroq addres berilga un agar variable ozgarsa copy ham ozgaradi 

#for loopi orqali dict ni con.log qilish
for key, value in players.items():
    print(key, value) #key and value bu variable dir ularni boshqa nom bn nomlasa boladi
#ham da setdefault() functioni orqali 'key' ni ozini dict ga qoshse boladi 'value' si esa None boladi
#dict da keylar unical boladi










