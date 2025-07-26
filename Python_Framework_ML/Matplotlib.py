import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\CMC\\artificial_intelligence\matplotlib\data3.csv')

print(df.columns) # Index(['Car_Name', 'Year', 'Price', 'Fuel_Type', 'Transmission', 'Number'], dtype='object')
font = {'family':'serif','color':'darkred','size':23}

print("Biểu đồ đường")
#plt.plot(df['Car_Name'], df['Number'], marker='h', ms=2) # ms là markers size , mec là markers color 
plt.subplot(1, 2, 1) # 1 row, 2 columns, and this plot is the first plot
plt.plot(df['Car_Name'], df['Number'], 'h--g', mec = 'hotpink', linewidth = '1') 
plt.title('Số lượng xe theo Car_Name', fontdict=font)
plt.xlabel('Car_Name')
plt.ylabel('Number')

print("Biểu đồ cột")
plt.subplot(1, 2, 2) # 1 row, 2 columns, and this plot is the second plot.
plt.bar(df['Car_Name'], df['Number'])
plt.title('Số lượng xe theo Car_Name')
plt.xlabel('Car_Name')
plt.ylabel('Number')

plt.show()


# # Vẽ biểu đồ cột
# print("Biểu đồ cột")
# plt.bar(df['Car_Name'], df['Number'])
# # Thêm tiêu đề và nhãn cho trục
# plt.title('Số lượng xe theo Car_Name')
# plt.xlabel('Car_Name')
# plt.ylabel('Number')
# # Hiển thị biểu đồ
# plt.show()


# # Vẽ biểu đồ phân tán (Scatter Plot)
# print("Biểu đồ phân tán")
# plt.scatter(df['Car_Name'], df['Price'])
# # Thêm tiêu đề và nhãn cho các trục
# plt.title('Biểu đồ phân tán giữa Car_Name và Price')
# plt.xlabel('Car_Name')
# plt.ylabel('Price')
# # Hiển thị biểu đồ
# plt.show()


# # Vẽ biểu đồ tròn (Pie chart)
# print("Biểu đồ tròn")
# car_sum = df.groupby('Car_Name')['Number'].sum()
# plt.pie(car_sum, labels=car_sum)
# # Thêm tiêu đề
# plt.title('Tỷ lệ số lượng xe theo Car_Name')
# # Hiển thị biểu đồ
# plt.show()


# # Vẽ biểu đồ tần suất
# plt.hist(df['Number']) # số cột có thể chỉnh bằng bins=số cột 
# plt.title("Phân Phối Số Lượng Xe Đã Bán (Number Distribution)")
# plt.xlabel("Số Lượng Xe (bins)")
# plt.ylabel("Tần Suất (Frequency)")
# plt.show()

