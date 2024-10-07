# 06 ลิสต์เรียงหรือไม่

def check_order(l:list,sort_l:list,rsort_l:list) -> str:
    if sort_l == rsort_l: # 4 
        ans = "The list is in non-increasing and non-decreasing order."
    elif sort_l == l: 
        ans = "The list is in non-decreasing order."
    elif rsort_l == l:
        ans = "The list is in non-increasing order."
    else:
        ans = "The list is in random order."
    return ans

ls = []
sort_ls = []
rsort_ls = []

# ls setup
while True:
    num = int(input("Enter a number (-1 to end): "))
    if num == -1:
        break
    if 0 <= num <= 100:
        ls.append(num)
        sort_ls.append(num)
        rsort_ls.append(num)
    else:
        print("Number is out of range.")

sort_ls.sort()
rsort_ls.sort(reverse=True)

if len(ls) != 0:
    print('-----\nOriginal list:')
    print(ls)
    print(check_order(ls,sort_ls,rsort_ls))
else:
    print('-----\nOriginal list:')
    print(ls)
    print("The list is empty.")