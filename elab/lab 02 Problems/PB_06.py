# พิมพ์ดาวบรรทัดเดียวสลับกัน

n = int(input())
char_1 = str(input())
char_2 = str(input())

# printing by no using string slice
char_long_size = (char_1 + char_2) * (n//2) + char_1 *(n%2)

print(char_long_size)