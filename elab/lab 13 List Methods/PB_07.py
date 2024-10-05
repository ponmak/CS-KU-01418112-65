# 07 List and String 3 

def extract_string(text:str) -> list:
    ls = []
    temp_str = ""
    for i in range(len(text)):
        if temp_str == "":
            temp_str += text[i]
        elif text[i].isnumeric() and temp_str[0].isnumeric():
            temp_str += text[i]
        elif (not text[i].isnumeric()) and (not temp_str[0].isnumeric()):
            temp_str += text[i]
        else:           
            ls.append(temp_str)
            temp_str = ""
            temp_str += text[i]
        
    new_ls = []
    for i in range(len(ls)):
        if ls[i].isnumeric():
            ls[i] = int(ls[i])

        #print(temp_str)
    ls.append(temp_str)
    return ls

print( extract_string("G2X3t4") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )
