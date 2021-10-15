number = int(input('Enter a number'))

reversed_number = 0
tmp_original = number#121

while tmp_original > 0:
    reversed_number = (reversed_number * 10) + tmp_original % 10
    tmp_original = tmp_original // 10
if number == reversed_number:
    print('This is Pallindrome')
else: 
    print('No Pallindrome')


s = input('Enter the value: ')

reverse = s[::-1]

if(s==reverse):
    print('Yes it is palindrome')
else: 
    print('No it si no Palindrome')

#num = [0,1,2,3,4,5,6,7,8,9]
#print(num[:-1:-1])















