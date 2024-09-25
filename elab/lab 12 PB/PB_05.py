# 05 Hangman 2

quest = input()
ans_list = []
while True:
    ans = input()
    
    if ans == "0":
        break

    ans_list.append(ans)

final_display = ""

for i in range(len(quest)):
    if quest[i] not in ans_list :
        final_display += quest[i].replace(quest[i], "-")
    else:
        final_display += quest[i]
    #print(f"final_display :  {final_display}")

print(final_display)
        