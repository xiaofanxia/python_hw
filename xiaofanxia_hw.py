#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:36:16 2020

@author: Xiaofan Xia
"""
# Problem1
#a
a=list(range(1,21));
print(a);
#b
b=a[::-1];
print(b);
#c
c=a+b[1:];
print(c);
#d
d=10*[4,6,3];
print(d);
#e
e=11*[4,6,3]
del e[31:33]
print(e);

#Problem2
import numpy as np;
import math as math;
items=np.arange(3,6.1,0.1);
l1=map(lambda x:(math.exp(x))*(math.cos(x)), items)
l1=list(l1)
print(l1)

#Problem3
items2=list(range(1,26))
l2=map(lambda x: (2**x)/x,items2)
l2=list(l2)
print(l2)

#Problem4
#a
n=len(a)-1
items3=list(range(0,20))
l3=map(lambda i:a[i]-a[n-i],items3)
l3=list(l3)
print(l3)

#b
l4=[]
for x in a:
    if x % 2 == 0:
        l="True"
    else:
        l="False"
    l4.append(l)

print(l4)

#Problem5
#a
#[1,4)
lorem = open('lorem.txt', 'r')
count14=0
content=lorem.read()
str_val = content.split(' ')
for i in str_val:
    if len(i)>=1 and len(i)<=4:
        count14+=1

print(count14)

#[4,7]
lorem = open('lorem.txt', 'r')
count47=0
content=lorem.read()
str_val = content.split(' ')
for i in str_val:
    if len(i)>4 and len(i)<=7:
        count47+=1

print(count47)

#8 and greater
lorem = open('lorem.txt', 'r')
count8=0
content=lorem.read()
str_val = content.split(' ')
for i in str_val:
    if len(i)>=8 :
        count8+=1

print(count8)

#b
lorem = open('lorem.txt', 'r')
count_C=0
content=lorem.read()
for i in content:
    if i.isupper():
        count_C+=1

print(count_C)

    
    


 