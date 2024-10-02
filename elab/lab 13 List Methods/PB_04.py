# 04 List Methods 4 
 
# .count(ls) : count all item in list 
# .index(item) : find item's index in list

ls = []
while True:
    item = input()
    if item == '':
        break
    ls.append(float(item))

min_count = 0
used_list = []
used_list_idx = 0

for i in ls:
    if i not in used_list:
        count = ls.count(i)
        used_list.append(i)

        if min_count == 0 :
            min_count = count

        if count < min_count:
            min_count = count
            min_list_idx = used_list_idx

        used_list_idx += 1

print(used_list[min_list_idx], min_count)


