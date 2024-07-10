# เติมน้ำมัน

# length and volume
km = int(input())
volume = int(input())

# calu func
ka_times = km / (15 * volume * (50/100)) 
kuy_times = km / (15 * volume * (90/100)) 

print(int(ka_times) + 1)
print(int(kuy_times) + 1)

