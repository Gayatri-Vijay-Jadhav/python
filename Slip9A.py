class demo: 
    def Reverse(self): 
        self.myStr=input("Enter any String: ") 
    def output(self): 
        s=self.myStr 
        cnt=len(s) 
        i=cnt-1 
        revStr="" 
        while(i >= 0): 
            revStr=revStr + s[i] 
            i=i-1 
            print("String in Reverse:" , revStr) 
Obj=demo() 
Obj.Reverse() 
Obj.output()



# class Demo:
#     def sample(self):
#         self.str=input("Enter a string")
#     def accept():
#         a=self.str
#         n=len(a)
#         i = cnt-1
#         str2=" "
#         while(i >= 0):
#             str2 = str2 + a[i]
#             i=i-1
#             print("String in reverse: ", str2)
            
# obj=Demo()
# obj.sample()
# obj.accept()
