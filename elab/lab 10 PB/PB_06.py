# 06 ลบข้อมูลซ้ำในลิสต์

def remove_duplicates(t):
    new_list = []

    for item in t:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4]))