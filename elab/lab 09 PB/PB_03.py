# 03 การขยายพันธุ์ของแบคทีเรีย

def nb_year(p0, percent, aug, p) -> int:
    day = 0
    
    while p0 < p:
        p0 += int(p0 * (percent / 100) + aug)
        day += 1
    if p0 >= p: 
        return day
