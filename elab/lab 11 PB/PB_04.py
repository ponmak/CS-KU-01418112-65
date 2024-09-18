# 04 Hangman 1

word = input()

count = 0
used = []

while True:
    guess = input()
    
    if guess not in used:
        for char in word:
            if char == guess:
                count += 1
    
    used.append(guess)
    
    if guess == "0":
        break
    elif count == len(word):
        break

print(f"{count}/{len(word)}")