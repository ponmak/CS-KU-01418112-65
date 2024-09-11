# IWonderWhy problem 3 : Series โจทย์จากความทรงจำ : ขนาดอลันทัวริ่งยังเป็นเกย์ ทำไมคุณไม่ลองเป็นบ้างล่ะ?

# สร้าง func ที่ทำให้ n = k ; ทำให้ค่าของจำนวนเต็มทั้งสองมีค่าเท่ากัน โดยใช้เพียงแค่ ×2 และ −1 เท่านั้น

def main(n, k):
    # if n = k in the first place
    i = 0
    if n == k and i == 0:
        return 0
    else:
        i = 0

        while n != k:
            '''if n < k:
                if k % 2 == 0:
                    i+=1
                    print(f"(!) n : {n}")
                    if k % n != 0:
                        n -= 1
                    else:
                        n *= 2
                else:
                    i += 1
                    print(f"(!) n : {n}")

                    if (k+1) % n != 0:
                        n -= 1
                    elif k+1 == n:
                        n -= 1
                    else:
                        n *= 2

            else:
                n -= 1
                i += 1'''

            if k > n:


        return i

# input n, k
n = int(input())
k = int(input())

print(main(n,k))
