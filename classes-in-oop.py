# This is how we create the data variable , data , attribute inside the class

# class student:
#     def __init__(self):
#         name = "uzair"
#         self.name = "muhammad uzair"
#         self.address = 'abc'
#         self.id = 3347
# s1 = student()
# s2 = student()
# print(s2.name,s2.address,s2.id)
# print(s1.name)



class student:
    def __init__(self,name,address,id):
        
        self.address = address
        self.id = id
        self.name = name
    def study(self):
        print('I am '+self.name+' and right now i am coding oop concepts.')
    
    def play(self):
        print('I am '+self.name+' right now i am playing.')

# s1 = student('uzair','abc',03347)  hence you cannot start integer with zero unless you are writing an octal number(base 8)

s1 = student('uzair','abc',3347)
s2 = student('moiz','xyz',7688)


# print(s1.name, s1.address, s1.id)
# print(s2.name, s2.address, s2.id)

s1.play()
s2.study()
