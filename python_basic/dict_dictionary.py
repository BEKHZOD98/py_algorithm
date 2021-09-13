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
