# 04 List Methods 4 
 
# .count(ls) : count all item in list 
# .index(item) : find item's index in list

ls = []
while True:
    item = input()

    if item == '':
        break

    ls.append(float(item))

print(ls.count(min(ls)))



