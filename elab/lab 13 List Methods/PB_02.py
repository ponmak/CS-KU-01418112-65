# 02 List Methods 2

# .pop() : discard last item and return
# .pop(index) :  discard item in that index and return
# .remove(data) : remove data from list (no return)

ls = [i for i in range(-65, 45)]

def count_factors_3_7(ls):
    count = 0
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            count +=1

    return count
print(count_factors_3_7(ls))

def filter_factors_3_7(ls):
    new_ls = []
    new_ls_2 = []
    for item in ls:
        if item <= 0:
            continue
        elif item > 0 and (item % 3 == 0 or item % 7 == 0):
            new_ls.append(item)
        elif item > 0 and (item % 3 != 0 and item % 7 != 0):
            new_ls_2.append(item)
        
    return [new_ls,new_ls_2]

print(filter_factors_3_7(ls))