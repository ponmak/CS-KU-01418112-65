# 04 ฐานนิยม

def find_mode(l):
    ans_list = []
    ans_count = []

    for i in l:
        if i not in ans_list:
            ans_list.append(i)
            ans_count.append(1)
        else:
            j = 0
            while True:
                if ans_count[j] == i:
                    break
                else:
                    j += 1

            ans_count[j] += 1

        print(ans_list, ans_count)

scores = []

for _ in range(20):
    score = int(input("Enter score: "))
    if 0 <=score <= 10:
        scores.append(score)
    else:
        print("Score is out of range.")

print("-----")
print("Original list:")
print(scores)
print("Mode of scores:")
find_mode(scores)
