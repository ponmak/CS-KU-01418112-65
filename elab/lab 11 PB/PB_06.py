# 06 ถอดรหัสเด็กงี่เง่า

enc_word = input()
dnc_word = ""

# creating list of vowel
vowel = "AaEeIiOoUu"

i = 0
while i < len(enc_word): # for loop suck
    if enc_word[i] in vowel: # first check
        if i + 2 < len(enc_word) and enc_word[i+1] == 'p' and enc_word[i+2] == enc_word[i]: # second check 
            dnc_word += enc_word[i]
            i += 3 # skip enc section
        else:
            dnc_word += enc_word[i]
            i += 1
    else:
        dnc_word += enc_word[i]
        i += 1

print(dnc_word)
