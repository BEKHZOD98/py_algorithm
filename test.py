def gcd(a,b):
    while (b !=0):
        temp = b
        b = a% b
        a = temp
    return a

print("HCD(60, 28) = " ,gcd(60,28))
'''
def gcd(a,b):
    while (b !=0):
        temp = b
        b = a% b
        a = temp
    return a
'''
