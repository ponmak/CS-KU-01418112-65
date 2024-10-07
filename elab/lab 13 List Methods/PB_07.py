# 07 List and String 3 

def extract_string(text: str) -> list:
    ls = []
    temp_str = ""
    digit = text[0:1].isdigit()  
    
    for i in range(len(text)):
        if temp_str == "":
            temp_str += text[i]
        elif text[i].isdigit() == digit:  
            temp_str += text[i]
        else:
            if temp_str.isdigit():
                ls.append(int(temp_str))  
            else:
                ls.append(temp_str)  
            temp_str = text[i]  
            digit = text[i].isdigit()  
    
    if temp_str:  # Append the final segment
        if temp_str.isdigit():
            ls.append(int(temp_str))
        else:
            ls.append(temp_str)
    
    return ls


print( extract_string("G2X3t4") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )

