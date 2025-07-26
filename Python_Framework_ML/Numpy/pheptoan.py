import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Phép toán cơ bản của 2 mảng numpy 
arr = arr1 + arr2 # [5 7 9]
arr = arr1 - arr2 # [-3 -3 -3]
arr = arr1 * arr2 # [ 4 10 18]
arr = arr1 / arr2 # [0.25 0.4  0.5 ] 
print(arr)


""" 
VD: [1, 1, 2, 3, 2, 3, 2]
.mean() (1+1+2+3+2+3+2)/7=2 
.media() 1, 1, 2, (2), 2, 3, 3 
.mode() số 2 xuất hiện nhiều lần nhất 

var Phương sai.
std Độ lệch chuẩn.
sum Tổng số.
cumsum Tổng tích lũy của một mảng.
max, min Giá trị lớn nhất và nhỏ nhất của một mảng.
argmax, argmin Các chỉ mục của giá trị lớn nhất và nhỏ nhất. 
round(x, 2) # làm tròn x đến chữ số thập phân thứ 2
"""

print(arr.mean()) # 0.3833333333333333
print(f"{np.round(arr.mean(), 2)}") # 0.38 làm tròn 