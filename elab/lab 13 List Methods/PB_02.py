# 02 List Methods 2

# .pop() : discard last item and return
# .pop(index) :  discard item in that index and return
# .remove(data) : remove data from list (no return)

ls = [i for i in range(7)]

def count_factors_3_7(ls):
    count = 0
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            count +=1

    return count
print(count_factors_3_7(ls))

def filter_factors_3_7(ls):
    new_ls = []
    for item in ls:
        if item > 0 and (item % 3 == 0 or item % 7 == 0):
            new_ls.append(item)
            ls.remove(item)

    return new_ls, ls

print(filter_factors_3_7(ls))