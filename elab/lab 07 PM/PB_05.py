# 05 ตัวเลขในจำนวนเต็ม

num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

if num < 0:
    print("Invalid number.")

if digit < 0 or digit > 9:
    print("Invalid digit.")

times = 0


print(f"Digit {digit} occurs {times} times.")

    