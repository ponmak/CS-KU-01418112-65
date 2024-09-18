# 04 String Operators 4 in

print("P" in "Python")
print("T" in "Python")
print("p" not in "Python")
print("F" not in "Python")

needle = 'programming'
haystack = 'Fundamental Programming Concept'
print(needle in haystack)

choice = input("Select menu (A, B): ")
if (choice in 'Aa'):
    print('This is menu A')
elif (choice in 'Bb'):
    print('This is menu B')
else:
    print('Invalid menu: neither A nor B')
    
for letter in 'Python':
    print('Current Letter:', letter)
    
sentence = "Fundamental Programming Concept"
for ch in sentence:
    print(ch, end='|')
