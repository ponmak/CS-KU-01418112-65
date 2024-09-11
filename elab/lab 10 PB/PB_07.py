# 07 หมดสิทธิ์สอบ

exercises = int(input())
percent = float(input())
student_num = int(input())

done_exercises = [int(input()) for i in range(student_num)]

# find percent of all student    
percent_done =  [(done/exercises) * 100 for done in done_exercises]

count = 0
for done in percent_done:
    if done < percent:
        count += 1

print(count)
for i in range(len(percent_done)):
    if percent_done[i] >= percent:
        print(f"{i+1} {percent_done[i]:.2f}")
    else:
        print(f"({i+1}) {percent_done[i]:.2f}")