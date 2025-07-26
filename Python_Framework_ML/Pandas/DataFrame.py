import pandas as pd

# 1. Tao dataframe và gán chỉ mục (Name, age)
df = pd.DataFrame({"Name": ["Huong", "Nhung", "Anh"],
                  "age": [19, 18, 19]})
print(df) # 3x2 

# In ra full cột khi biết tên cột 
cot = df['Name']
print(cot)

# In ra 1 phần tử khi biết tên cột và index hàng 
print(df['Name'][2]) # Anh 

# 2. Tao dataframe và không gán chỉ mục
df = pd.DataFrame([["Huong", "Nhung", "Anh"], [19, 18, 19]])
print(df) # 3x2 
print(df[0]) # cột đầu tiên 
print(df[0][0]) # phần tử đầu tiên của bảng 
