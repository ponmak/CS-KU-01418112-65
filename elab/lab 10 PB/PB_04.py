# 04 ฐานนิยม

def find_mode(l):
    ans_list = []
    ans_count = []

    # set list for all ans
    for idx in l:
        if idx not in ans_list:
            ans_list.append(idx)
            ans_count.append(0)

    #print(ans_list)

    # bubble sort
    for i in range(len(ans_list)):
        for j in range(len(ans_list) - i - 1):
            if ans_list[j] > ans_list[j+1]:
                ans_list[j], ans_list[j+1] = ans_list[j+1], ans_list[j]

    #print(ans_list)

    # count every number
    for i in range(len(ans_list)):
        for j in range(len(scores)):
            if scores[j] == ans_list[i]:
                ans_count[i] += 1

    # print(ans_count)

    # print ans_list by finding index from max value in ans_count
    for i in range(len(ans_list)):
        if ans_count[i] == max(ans_count):
            print(ans_list[i])

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
