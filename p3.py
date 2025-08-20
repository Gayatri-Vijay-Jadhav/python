# a = lambda x, y: x + y, x - y
# print(a(5, 3))  
a = lambda x, y: (x + y, x - y, x * y, x / y)
print(a(5, 3)) 