# 03 ตัดสระในสตริง

word = input()

# creating list of vowel
vowel = "AaEeIiOoUu"

del_vowel = [char for char in word if char not in vowel] # recreate new text to list

# add text together

del_word = ""

for char in del_vowel:
    del_word += char
    
# or just .join
# del_word = "".join(del_vowel)

print(del_word)