x = (1,4,7,10) 
y = (2,5,8,11) 
z = (3,6,9,12) 
print("Original lists:") 
print(x) 
print(y) 
print(z) 
print("\nElement-wise sum of the said tuples:") 
result = tuple(map(sum, zip(x, y, z))) 
print(result) 

from numpy import array 
lst1=[1,5,7] 
lst2=[3,2,1] 
a = array(lst1) 
b = array(lst2) 
print(a + b) 