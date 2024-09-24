# 06 ถอดรหัสเด็กงี่เง่า

word = input()
new_word_list = []

# creating list of vowel
vowel = "AaEeIiOoUu"

for i in range(len(word)):
    if word[i] not in vowel and word[i] != 'p': # first check
        new_word_list.append(word[i])
    elif word[i] == 'p':
        if word[i+1] != word[i-1]:
           new_word_list.append(word[i])
    else:
        if i - 2 >= 0:
            if word[i-2] != word[i]:
                new_word_list.append(word[i])
        else:
            new_word_list.append(word[i])

print("".join(new_word_list))
