# 05  การประมูล 

dict_all = {}

while True:
    text = input()

    if text == "end":
        break

    name, money = text.split()
    money = float(money)

    if name not in dict_all.keys():
        dict_all[name] = [money , 1]
    else:
        temp_list = dict_all.get(name)
        dict_all[name] = [max(money, temp_list[0]), temp_list[1] + 1]

dict_all = dict(sorted(dict_all.items()))

for bid in dict_all:
    temp_list = dict_all.get(bid)
    if temp_list[1] != 1:
        print(f"{bid} bid at the price of {temp_list[0]:.1f} baht in {temp_list[1]} times.")
    else:
        print(f"{bid} bid at the price of {temp_list[0]:.1f} baht in {temp_list[1]} time.")

max_money = 0
max_name = ""
for bid in dict_all:
    temp_list = dict_all.get(bid)

    if temp_list[0] > max_money:
        max_money = temp_list[0]
        max_name = bid

print(f"The winner is {max_name}.")



