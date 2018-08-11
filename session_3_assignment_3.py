# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:26:56 2018

@author: disiz
"""
"""
-Session 3
-Assignment THREE
"""
##assignmnet 3 question 1.1
print("*/ assignment 3 output 1.1/*")

def myreduce(lst1):
    sum=0
    for i in range(0,len(lst1)):
        sum+=lst1[i]
    return(sum)
print("sum of list of numbers using myreduce() is:"+str(myreduce([1,2,3,4,5,6])))
print("-"*100)
print('\n')

"""
-Session 3
-Assignment THREE
"""
##assignmnet 3 question 1.2
print("*/ assignment 3 output 1.2/*")
lst_even_true=[]
def myfilter(num):
    lst_even_true=[]
    for i in range(num):
        if i%2==0:
            lst_even_true.append(i)
    return(lst_even_true)
print("list of even numbers using myfilter() is:\n"+str(myfilter(40)))
print("-"*100)
print('\n')
"""
-Session 3
-Assignment THREE
"""
##assignmnet 3 question 2
print("*/ assignment 3 output 2 - LIST comprehensions outputs /*")
len_list=[]
inp='ACADGILD'
lst=list(inp)
print(lst)
print("-"*100)
print('\n')
l=['x','y','z']
o_p0=[i*j for i in l for j in range(1,5) ]
print(o_p0)
print("-"*100)
print('\n')
o_p1=[i*j for i in range(1,5) for j in l ]
print(o_p1)
print("-"*100)
print('\n')
o_p2=[[j+i] for i in range(3) for j in range(2,5)]
print(o_p2)
print("-"*100)
print('\n')
o_p3=[[j,j+1,j+2,j+3] for j in range(2,6)]
print(o_p3)
print("-"*100)
print('\n')
o_p4=[(j,i) for i in range(1,4) for j in range(1,4)]
print(o_p4)
print("-"*100)
print('\n')
"""
-Session 3
-Assignment THREE
"""
##assignmnet 3 question 3
print("*/ assignment 3 output 3/*")
words_list=['abc','def','ghijk','lmnopq','rstuvwxyz']
len_list=[]
for i in words_list:
    len_list.append(len(i))
print("the longest word in the given list of words is:'{}'".format(words_list[len_list.index(max(len_list))]))    
print("-"*100)
print("End of assignment")

