#1. print 

print('Hello haha hihi')
# out 
# Hello haha hihi
# Run bằng terminal bằng lệnh python path_to_file.py

import sys

import data.kho_1 
print(sys.version)
# out
# 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)]

#2. Kiểu dữ liệu (tạo biến - creating variables)

x = "Mo"
x = 5 
#x = 5 + "MO" # run -> typeerror : unsupported operand type(s) for +: 'int' and 'str'
# no type and can change type after set 

y = str(3.9) # 3.9
y = int(3.9) # 3
y = float(3.9) # 3.9 

print(x, y) # 5 3.9
print(x+y) # 8.9 

# Nâng cao về kiểu dữ liệu 
z = 2+3j #complex số phức (.real, .imag)
z = ["apple", "banana", "cherry"] #list 
z = ("apple", "banana", "cherry") #tuple 
z = {"name" : "John", "age" : 36} #dict 
z = {"apple", "banana", "cherry"} #set 
#mo=iter(z), next(mo) , __iter__() & __next__()
#mv = memoryview(z) #thay đổi trực tiếp trong z, không cần tạo bản sao . Dùng khi Cần tốc độ cao + tránh sao chép (copy)
z = "Huong"
print(z[1:2]) #u 
print(z.replace("g", "?")) # Huon? , thay thế 
print(z[-2:-1]) #n 
print(z.upper)
print(z.lower)
print(z.lower)


#3. Hàm (function)
def cocul(a, b):
    print(a+b)

cocul(x, y) # 8.9 

# Operators 

# and, or, not 
# is, is not, in, in not, 

#4. lambda 
# https://www.w3schools.com/python/python_lambda.asp

#5. Hàm tạo __init__()

class Animal:
    def __init__(self, name):
        print("Animal init")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Gọi __init__ của Animal
        print("Dog init")
        self.breed = breed

#6. Modules 
import data
x = data.kho_1.food["name"]
print(x) # icream

#7. Datetime thời gian 
import datetime 
print(datetime.datetime.now()) # 2025-07-25 08:40:13.531646
print(datetime.datetime.now().year) # 2025
print(datetime.datetime(2005, 7, 23, 1, 2, 3, 4)) # 2005-07-23 01:02:03.000004





