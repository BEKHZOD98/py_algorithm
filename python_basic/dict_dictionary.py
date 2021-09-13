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
del players['So'] #orqali delete qisa boladi
print(players)




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

