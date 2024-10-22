# 06 ขาดเรียนและหมดสิทธิ์สอบ

set_test = input().split()
set_test = sum([int(i) for i in set_test])

pass_ = input().split()
pass_dict = {"come":float(pass_[0]), "submit":float(pass_[1])}

num = int(input())

student_dict = {}
for i in range(num):
    comein = input()

    # percent
    zero = comein.count("0")
    one = comein.count("1")
    percent = (one / (zero + one)) * 100

    student_dict.update({i:percent})

for i in range(num):
    submitin = input().split()
    submitin = sum([int(i) for i in submitin])

    percent = (submitin / set_test) * 100

    student_dict[i] = {"comein" : student_dict[i], "submitin":percent}

#print(student_dict)

cant_pass = 0
for i in range(num):
    if pass_dict["come"] > student_dict[i]["comein"] and pass_dict["submit"] > student_dict[i]["submitin"]:
        cant_pass += 1

print(cant_pass)

for i in range(num):
    if pass_dict["come"] > student_dict[i]["comein"] and pass_dict["submit"] > student_dict[i]["submitin"]:
        print(f"({i+1}) {student_dict[i]["comein"]:.2f} {student_dict[i]["submitin"]:.2f}")
    else:
        print(f"{i+1} {student_dict[i]["comein"]:.2f} {student_dict[i]["submitin"]:.2f}")