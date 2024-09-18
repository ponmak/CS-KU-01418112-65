# 02 นับสระในสตริง

word = input()

# creating list of vowel
vowel = "AaEeIiOoUu"

count = 0
for i in range(len(word)):
    if word[i] in vowel: # just like find item in list
        count += 1

print(count)