# 03 List Methods 3 

# .sort() / .sort(reverse=True) / .reverse()

def filter_sort_factors_3_7(ls):
    new_ls = []
    new_ls_2 = []
    for item in ls:
        if item <= 0:
            continue
        elif item > 0 and (item % 3 == 0 or item % 7 == 0):
            new_ls.append(item)
        elif item > 0 and (item % 3 != 0 and item % 7 != 0):
            new_ls_2.append(item)

    new_ls.sort()
    new_ls_2.sort(reverse=True)
    return [new_ls, new_ls_2]

ls = [i for i in range(-65, 45)]
print(filter_sort_factors_3_7(ls))