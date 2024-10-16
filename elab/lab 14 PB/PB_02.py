# 02 Cloth Size

def cloth_size(width_list) -> dict:
    result = {'S': 0, 'M': 0, 'L': 0}
    
    for size in width_list:
        if size <= 36:
            result['S'] += 1
        elif size > 44:
            result['L'] += 1
        else:
            result['M'] += 1
    return result

print(cloth_size([50, 44, 40, 48]))

