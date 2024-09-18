# 06 ถอดรหัสเด็กงี่เง่า

word = input()

# creating list of vowel
vowel = "AaEeIiOoUu"

word_ls = []

for i in range(len(word)):
    word_ls.append(word[i])
    
    if word[i] in vowel:
        word_ls.append("p")
        word_ls.append(word[i])

print("".join(word_ls))

