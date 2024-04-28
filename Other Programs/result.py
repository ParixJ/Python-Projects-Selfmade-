
eng = int(input("Enter Engilsh Marks "))
sci = int(input("Enter Science Marks "))
ss = int(input("Enter SS Marks "))

def res(eng,sci,ss):
    if eng > 40 :
        if sci > 40 :
            if ss > 40 :
                result = print("PASS")
    else :
        result = print("FAIL")
    return result
          
            
result = res(eng,sci,ss)




