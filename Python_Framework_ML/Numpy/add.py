import numpy as np 

# Mảng 1 chiều 
arr = np.array([1, 2, 3])
print(arr) # [1 2 3]

arr = np.append(arr, [4, 5, 6])
print(arr) # [1 2 3 4 5 6]

# Mảng 2 chiều 
arr = np.array([[1, 2], [3, 4], [5, 6]]) # 3x2 
    # axis = 0 -> Thêm 1 hàng 
    # axis = 1 -> Thêm 1 cột 
    # Phần tử thêm vào hàng / cột thì ma trận chứa ptu thêm có cột / hàng cố định 
arr = np.append(arr, [[7,8]], axis=0) # [[1 2] [3 4] [5 6] [7 8]]
print(arr)

# Mảng 3 chiều 