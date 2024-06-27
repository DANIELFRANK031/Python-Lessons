#print('Hello World')
a=5
b=10
c=a+b
#print(c)
if a > b: 
    print('a is greater than b')
else:
    print('a is not greater than b')

def numbercheck(number):
    if number%2==0 and number < 10:
        print('True and less than 10')
    else:
         print('The number is odd')


numbercheck(9)