# a = 5
# print(type(a))

# b = 5.5
# print(type(b))

# c = "uzair"
# print(type(c))
# c = c.capitalize()
# print(c)
# d = "5"
# print(type(d))


# class bike:
#     pass

# print(bike)


# a = 5+6j
# print(a.real)
# print(a.imag)
# s1 = ['xyz']
# print(s1)
# s1.append("abc")
# print(s1)

# s1 = [1,2,3,4]
# s1.append([5,6,2,1])
# print(s1)


# class bike:
#     pass

# YBR = bike()
# print(YBR)
# print(type(YBR))

class bike:
    def __init__(arg1):
        print(id(arg1))
        print("i will be automatically call when the object is created")

YBR = bike()
print(id(YBR))

