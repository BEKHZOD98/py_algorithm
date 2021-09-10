int_list = [1,2,3]
mixed_list = [1,2.0,'string']
print(len(int_list))
print(mixed_list[-1])
print(mixed_list[1:])
names1 = ['John','Bob','Alice']
names2 = ['Tracy','Elijah','Mason']
names_combined=names1+names2
print(names_combined)#2ta listni qoshib chiqarsa ham boladi
print(type(names_combined))
names1[1] = 'abbos'
print(names1)
names1.append('william') #append() orqali listga index qoshse boladi
names1.append(2.0)
print(names1)
print(len(names1))
popped = names1.pop() #if qavs ichi bosh bolsa by default listni oxirgi index keyi ochiriladi
print(popped)
print(names1)
names1.pop(0) #agar biza index boylab ochirish k-k bosa pop ichiga index beriladi
names1.sort()#orqali biza A-Z gachon sort qilib beradi
print(names1)
letters = ['az','aj','ab', 'ak']
letters.sort()
print(letters)
letters = ['abcd','az','abc']
letters.sort(key=len)#agarda sort()ni ichiga key=len berilsa o'sish ketma ketligi bo'yicha  print qilinadi
                     #agarda letters.reverse() qilinsa teskarisiga chiqarib beradi kamayishga emas balki faqat gina teskarisigadir
letters.reverse()
num = [2,3,1,64,4225,4,6,1,1,5,6]
num.sort(reverse=True) #bolsa unda kamayishga qarab chiqarib beradi
print(letters)
print(num)
#hamda biz num.append() orqali listni oxirgi indexsiga key qoshmasdan index nomerini berib hohlagan qismimizga qoshsak boladi
num.append('william') 
num.insert(1,'abbos')#bunda insert()funksiyasini birinchi argumantiga index berilib, 2 oargumentiga object beriladi.
#num.index(value,start= stop=)function star and stop bu index nomeri beriladi value esa listni key dir
#count()functionni list dagi o'xshash objectlar sonini qaytaradi
print(num.count(1))
print(num)
#list ni nusxasini olish num.copy() copy functioni orqali nusxa olinib song num variablesini o'zgartirsak copy qilganimiz ham o'zgaradi
num.clear()# bu listdagi barcha indexlarni delete qilib tashlidi
