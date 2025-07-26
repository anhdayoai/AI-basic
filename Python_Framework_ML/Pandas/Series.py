import pandas as pd
import numpy as np 

# Tạo series (mảng 1 chiều) từ list  
my_list = [1, 2, 3]
arr = pd.Series(my_list)
print(arr) # có index từ 1 đến 2 , còn numpy sử dụng đượng nhưng in ra thì gần như list

# Tạo series (mảng 1 chiều) từ mảng 1 chiều numpy 
arr = pd.Series(np.array(my_list))
