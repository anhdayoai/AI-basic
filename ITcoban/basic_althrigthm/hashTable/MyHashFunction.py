# Bản chất của hàm băm là một hàm biến đầu vào có kích thước bất kỳ → thành một giá trị đầu ra có kích thước cố định

def simple_hash(s, size=8):
    result = 0
    for i, c in enumerate(s):
        result += (i + 1) * ord(c)
    result = result % (10 ** size)
    if len(str(result)) != 8 :
        x = 8 - len(str(result))
        result = result*(10**x)
    return result 

# Ví dụ:
password = "hfowhfhhf"
hashed = simple_hash(password)

print("Giá trị băm:", hashed) # 47270000
