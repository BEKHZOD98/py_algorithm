my_set = set()
print(type(my_set))
my_set.add(1)
print(my_set)
my_list = [1,1,1,1,2,2,2,2,3,3,3,4]
print(my_list)
s = set(my_list)
print(s)#set() functioniga berilgan valuelar unical turda boladi
set1 = {1,2,3,4}
set2 = {1,2,3,4,5}
print(set1.issubset(set2))#issubset() functionni set1 dagi elementlar set2da bolsa u True qaytaradi
print(set2.issubset(set1))#bu yerda False qaytadi chunki 5 set1da yoq
print(set2.issuperset(set1))#buyerda esa issuperset orqali set2dagi koplik set1da kop ligi unchun True qaytardi
set_one = {1,2,3}
set_two = {4,5,6}
print(set_one.isdisjoint(set_two))#qachonki set_one va set_two ni ichidagi koplik bir biridan 100%farq qilsagina true qaytaradi
set_3 = set1.union(set2)#bu birlashma functioni dir unical birlashma
print(set_3)
set_3 = set1.intersection(set2)#intersection() bu ikkita set ni ichidagi bir xil bor bolgan value larni gina return qiladi
print("peresicheniya: ",set_3)
#difference() va simmetric_difference() set3 = set1.difference(set2) bunda faqatgina set1ni gina set2ga nisbatan boshqacha bolgan valuesini return qiladi
#set3 = set1.simmetric_difference(set2) esa set1 va set2 birbirida ozaro bolmagan value larni return qiladi

#update() functioni sintaksisi haqida set1.update(set2) set1ni update qiladi yoq narsa ni chiqarib beradi

'''setdagi bir dona element ni ochirish un remove() , discard(bu funcda yoq elementni ochirilsa error chimidi) va pop(bu esa random element ni ochiradi),
    hamda clear() functioni orqali koplikni hamma valuesini ochirsak boladi
'''
