import numpy as np 

# list trong python 
my_list = [1, 2]
my_list.append(3)
print(my_list) # [1, 2, 3]

arr = np.array(my_list)
print(arr) # [1 2 3]
print(type(arr)) # <class 'numpy.ndarray'>

# tuple trong python
my_tuple = (1, 2)
add_tuple = (3, )
my_tuple += add_tuple
print(my_tuple) # (1, 2, 3) 

arr = np.array(my_tuple)
print(arr) # [1 2 3]

# dict trong python 
my_dict = {'one': 1, 'two': 2}
print(my_dict) # {'one': 1, 'two': 2}

arr = np.array(my_dict)
print(arr) # {'one': 1, 'two': 2}

# set trong python 
my_set = {1, 4, 5, 2, 3, 4, 4, 3}
print(my_set)
print(type(my_set))
arr = np.array(my_set)
print(arr)

# Kích thước mảng numpy 
#print(len(arr))
print(arr.size)

# Tạo mảng tuần tự 
arr = np.arange(2) 
print(arr) # [0 1]

# Tạo mảng với hiệu 2 giá trị cạnh nhau luôn bằng nhau 
arr = np.linspace(1, 10, 4) # khoangcach = (dau - cuoi) / (soluong - 1)
print(arr) # [ 1.  4.  7. 10.]

# Tạo mảng có giá trị nguyên bất kỳ từ 0 đến 10 , kích thước 5
arr = np.random.randint(0, 11, size=5)

# Chuyển ma trận 1 chiều thành 2 chiều 
    # arr = [ 1.  4.  7. 10.]
arr = np.arange(9).reshape(3, 3)
print(arr)
print(arr[0][0]) # 0 