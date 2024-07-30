# 05 ตัวเลขในจำนวนเต็ม

num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

times = len(str(num)) // digit

if (num < 0) and (digit < 0 or digit > 9):
    print("Invalid number.")
    print("Invalid digit.")
elif num < 0:
    print("Invalid number.")
elif digit < 0 or digit > 9:
    print("Invalid digit.")
elif times == 1:
    print(f"Digit {digit} occurs {times} time.")
else:
    print(f"Digit {digit} occurs {times} times.")



    