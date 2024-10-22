# 04 Chemical Formula

def extract_atoms(formula) -> dict:
    atoms_dict = {}
    st, num = '', ''
    st = formula[0]

    for i in range(1, len(formula)):
        ch = formula[i]
        if ch .isalpha():
            if ch.isupper():
                if num == '':
                    num = 1
                atoms_dict[st] = num
                st, num = ch, ''
            else:
                st += ch
        else:
            num += ch
    
    if num == '':
        num = '1'
    atoms_dict[st] = num

    return atoms_dict
 
formula = input()
atom = input()
atoms = extract_atoms(formula)
print(atoms.get(atom,0)) # when atom is not in formula return 0