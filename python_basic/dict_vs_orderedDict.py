d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['d'] = 'D'

d2 = {}
d2['a'] = 'A'
d2['d'] = 'D'
d2['b'] = 'B'
print(d1==d2)

from collections import OrderedDict
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['d'] = 'D'
#OrderedDict orqali dict ni semantic ketma ketligini solish tiriladi True chiqish un k-k bir xil bolish shart
d2 = OrderedDict()
d2['a'] = 'A'
d2['d'] = 'D'
d2['b'] = 'B'
print('orderedDict()',d1==d2)