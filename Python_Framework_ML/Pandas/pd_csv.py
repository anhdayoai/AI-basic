import pandas as pd 
import numpy as np 

df = pd.read_csv('D:\CMC_Ky4\CODE\Python\cmc\ThiGK\data3.csv')

print("Thông tin file")
print(df.info())

print("In ra 5 phần tử đầu tiên")
print(df.head())

print("In ra 10 phần tử đầu tiên")
print(df.head(10))

print("In ra 5 phần tử cuối cùng")
print(df.tail())

print("In ra phần tử có index từ 3 đến 5")
print(df.iloc[3: 6])

print("Tên các cột")
print(df.columns) # Index(['Car_Name', 'Year', 'Price', 'Fuel_Type', 'Transmission', 'Number'], dtype='object')

# In ra thông tin 1 cột với tên 
cot = df['Car_Name']
print(cot)

# In ra thông tin 2 cột 
cots = df[['Car_Name', 'Number']]
print(cots)

    # Tạo bảng từ 2 cột 'Car_Name', 'Number'
table = df.loc[:, ['Car_Name', 'Number']]
print(table)

# Kết nối nội 
    # pd.merge(df1, df2, left_on='Key_in_df1', right_on='Key_in_df2', how='join_type') giống SQL inner, left, right, outer 
df_merge = pd.merge(df, table, left_on='Car_Name', right_on='Car_Name', how='inner')

# Hợp nhất pd.concat([df1, df2], axis=0, sort=True) // axis=0 là liên kết theo chiều dọc , axis=1 là liên kết theo chiều ngang 

# Sắp xếp 
    # 1 cot
    # df.sort_values(by='Tên_cột', ascending=True hoặc False)
    # True tăng dần, False giảm dần 
# Sắp xếp df theo thứ tự tăng dần của Number 
df_numbertrue = df.sort_values(by='Number', ascending=True)
print(df_numbertrue)
    # 2 cot 
    # df.sort_values(by=['Tên_cột_1', 'Tên_cột_2'], ascending=[True hoặc False, True hoặc False])
    # Có ưu tiên cột 
# Sắp xếp df theo thứ tự tăng dần của Number và giảm dần của 'Car_Name'
# Sắp xếp theo 'Number' (tăng dần)
# Nếu hai dòng có giá trị trong cột Number giống nhau, Sắp xếp theo 'Car_Name' (giảm dần)
df_2cot = df.sort_values(by=['Number', 'Car_Name'], ascending=[True, False])
print(df_2cot)

# groupby nhóm dữ liệu theo một hoặc nhiều cột và sau đó thực hiện các phép toán thống kê hoặc tổng hợp trên các nhóm đó
    # Các phép toán có thể là 
        # sum(): Tính tổng.
        # mean(): Tính giá trị trung bình.
        # count(): Đếm số lượng phần tử trong mỗi nhóm.
        # min(): Tìm giá trị nhỏ nhất.
        # max(): Tìm giá trị lớn nhất.
        # std(): Tính độ lệch chuẩn.
    # df.groupby('cột_group').agg(...)

