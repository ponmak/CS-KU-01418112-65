# 04 Chemical Formula

def extract_atoms(formula) -> dict:
    atoms_dict = {}
    temp = ""
    num = ""
    for i in range(len(formula)):
        if formula[i].isalpha():
            if formula[i].isupper():
                if num = '':
                    num = '1'
        else:
            num += formula[i]
    return atoms_dict
 
formula = input()
atom = input()
atoms = extract_atoms(formula)
print(atom)
print(atoms.get(atom,0)) # when atom is not in formula return 0