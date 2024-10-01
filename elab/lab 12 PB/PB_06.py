# 06 เปลี่ยนจำนวนเงินให้เป็นตัวเลข

num = input()

ERROR_SIGN = "ERROR"
error = False
count = 0

if ',' in num and '.' not in num: #no floating point
    joiner = ""
    front = False
    for seg in num:

        if count != 3 and front and seg ==',':
            error = True
            break
        
        if seg in "0123456789":
            count += 1
 
        if seg not in  "0123456789" and seg !=',' or count > 3:
            error = True
            break

        if seg != ',':
            joiner += seg
        elif front and seg != ',':
            joiner += seg
            count +=1
        elif seg == ',' :
            front = True
            count = 0
    
    #print(count)
    if count != 3 and front :
        error = True
        

    if error == False:
        print(int(joiner) + 1)
    else:
        print(ERROR_SIGN)

elif '.' in num : # floating point 
    point = False
    error = False
    joiner = ""
    front = False
    point_count = 0
    count = 0
    if ',' in num:
        for seg in num:

            if seg == '.':
                if count != 3 and front :
                    error = True
                    break
                joiner += seg
                point = True
                front = False
                count = 0
            elif point:
                joiner += seg
                point_count += 1

            if count != 3 and front and seg ==',':
                error = True
                break

            if (seg not in  "0123456789" and (seg !=',' and seg != '.') or count > 3) or point_count > 2:
                error = True
                break

            
            if seg != ',' and point == False:
                joiner += seg
                count +=1
            elif front and seg != ',' and point == False:
                joiner += seg
                count +=1
            elif seg == ',' and point == False:
                front = True
                count = 0

            #print(count, joiner)
        #print(count)
        if count != 3 and front :
            error = True

        # display
        if error == False :
            if len(joiner) == len(str(int(float(joiner)))) + 2:
                print(f"{float(joiner) + 1:.1f}")
            else:
                print(f"{float(joiner) + 1:.2f}")
        else:
            print(ERROR_SIGN)

    else:
        error = False
        joiner = ""
        front = False
        point = False
        point_count = 1
        for seg in num:
            if (count != 3 and front and seg ==',') or (point_count > 2):
                error = True
                break

            if seg not in "0123456789.":
                error = True
                break

            if seg == '.':
                joiner += seg
                point = True
            elif point:
                joiner += seg
                point_count += 1
            else:
                joiner += seg

        # display
        if error == False :
            if len(joiner) == len(str(int(float(joiner)))) + 2:
                print(f"{float(joiner) + 1:.1f}")
            else:
                print(f"{float(joiner) + 1:.2f}")
        else:
            print(ERROR_SIGN)

else:
    print(int(num) + 1)
 