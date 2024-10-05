# 01 name, name & name 

def namelist(names: list) -> str:
    ans = ""

    if len(names) == 0:
        return ''

    if len(names) == 1:
        return names[0]

    for i in range(len(names)):
        if names[i] != names[-1] and names[i] != names[-2] :
            ans += names[i] + ', '
        elif names[i] == names[-2]:
            ans += names[i] + ' & '
        else:
            ans += names[i]

    return ans
