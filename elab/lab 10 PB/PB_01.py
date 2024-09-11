# 01 Histogram

scores = []
i = 0
while i < 20:
    score = int(input("Enter score: "))

    if score > 10 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
        i += 1

print("Original list:")
print(scores)

i = 0
while i < 11:
    count = 0
    for score in scores:
        if score == i :
            count += 1

    print(f"{i:>2} {'*'*count}")

    i += 1
