'''
Created on 22-Feb-2026

@author: HP
'''
from conda.common._logic import TRUE
from sqlalchemy.sql.expression import false
a=20
b=3
c=a+b
print((c))
d=a*b
print((d))
e=a-b
print((e))
f=a/b
print((f))
g=a%b
print((g))
h=a**b
print((h))
i=a//b
print((i))


a=10000
b=20000
c= a>b
print((c))

c=b>a
print((c))

c=b==a
print((c))

c=b>=a 
print((c))

c=b<=a 
print((c))

c= b!=a 
print((c))

a= True
b=False

c=a and b
print((c))

d= false
e= True 
f= not(d and e)
print (f)


print ('SRI'in "SRINIDHI")

a=b=10
print(a is b)


a= input("Please enter a number: ")
b=input("please enter another number:")
c=a+b
print(f"sum of {a} and {b}is",c)
