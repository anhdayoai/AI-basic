import time

start_time = time.time()
# Đoạn mã bạn muốn đo
for i in range(1000000):
    pass
end_time = time.time()

print("Thời gian chạy:", end_time - start_time, "giây")
