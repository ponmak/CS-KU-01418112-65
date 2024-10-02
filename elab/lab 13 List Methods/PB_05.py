# 05 List and String 1

#  .split(delimeter)

text = input()
ls = text.split('.')

text =input()
ls = text.split('.')
ls = [int(i) for i in ls]

xy_1 = input().split(',')
xy_2 = input().split(',')
print(f"{(float(xy_1[0]) + float(xy_2[0]))},{(float(xy_1[1]) + float(xy_2[1]))}")