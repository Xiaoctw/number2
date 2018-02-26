import Sort
import random
a=[3,2,4,5,7,7,32,5,3,5]
b= Sort.insert_sort(a)
print(b)
a=[3,2,4,5,7,7,32,5,3,5]
c=Sort.select_sort(a)
print(c)
d=Sort.quick_sort(a,0,len(a)-1)
print(d)
e=[]
e=[4,3,6,4,21,53,2,4,2,6,8,33,5,3,2,6]
s=Sort.shell_sort(e[:])
print(e)
print(s)