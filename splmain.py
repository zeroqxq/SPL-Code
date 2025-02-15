# SPL | Simple program language
import os 
digits = "123456789"
vars = {}
def printer(arlis : list):
    tot = ""
    for x in arlis:
        str(x)
        x = x.strip()
        if x == "/n":
            tot = tot + "\n"
        elif (x.startswith('"') and x.endswith('"')):
            x =  x.replace('"' , "")
            x = str(x)
            tot = tot + x + " "
        elif (x.startswith("'") and x.endswith("'")):
            x =  x.replace("'" , "")
            x = str(x)
            tot = tot + x + " "
        elif not (x.startswith('"') and x.endswith('"')) or (x.startswith("'") and x.endswith("'")):
            if x.isdigit() == True:
                str(x)
                tot = tot + x + " "
            else:
                if x in vars.keys():
                    tot = tot + str(vars[x]) + " "
                else:
                    raise Exception("Code[er01] Missing - ' ")
    print(tot)

def spl_input(k=""):
    if k != "":
        if not (k.startswith('"') and k.endswith('"')) or (k.startswith("'") and k.endswith("'")):
            raise Exception("Code[er01] Missing - ' ")
        elif k.startswith('"') and k.endswith('"'):
            k = k.replace('"', "")
        elif (k.startswith("'") and k.endswith("'")):
            k = k.replace("'", "")
    user_input = input(k)
    return user_input

def interpriter():
    global func, com
    com = input(" >> ")
    if com.startswith("#"):
        interpriter()
    cr_var()
    if "(" in com and ")" in com:
        com = com.replace(")" , "")
        comsp = com.split("(")
        func = comsp[0]
        func = func.strip()
        if func == "print":
            args = comsp[1].strip()
            args = args.split(",")
            printer(args)
        elif func == "delv":
            args = comsp[1].split(",")
            for el in args:
                del vars[el]
        elif func == "read":
            comment = comsp[1]
            spl_input(comment)
        elif func == "clear":
            main()
        elif func == "type":
            varntype = comsp[1]
            spl_type(varntype)
        elif func == "intconvert":
            vctoint = comsp[1]
            spl_intconvert(vctoint)
        elif func == "strconvert":
            strconv = comsp[1]
            spl_strconvert(strconv)
        elif func == "floatconvert":
            fconv = comsp[1]
            spl_floatconvert(fconv)
        else:
            raise Exception("Code[er03] - Invalid comand")
        
def cr_var():
    global com 
    infunc = ""
    if "=" in com:
        comsp = com.split("=")
        varn = comsp[0].strip()
        varv = comsp[1].strip()
        if varv.startswith("read"):
            varv = varv.replace(")", "")
            inspl = varv.split("(")
            infunc = inspl[0].strip()
            argcomment = inspl[1].strip()
            com = com.replace(")", "")
            com = com.replace("(", "")
        if varn[0] in digits:
            raise Exception("Code[er02] ; A variable cannot start with a number ")
        else:
            if varv in vars.keys():
                varv = vars[varv]
                vars.update({varn : varv})
            elif infunc == "read":
                input_val = spl_input(argcomment)
                vars.update({varn : input_val})
            elif '+' in varv or "-" in varv or "/" in varv or '*' in varv or "**" in varv:
                ev = ""
                for el in vars.keys():
                    if el in varv:
                        varv = varv.replace(el, str(vars[el]))
                comli = list(varv)
                comli = [w for w in comli if w.strip()]

                for el in comli:
                    if el in vars.keys():
                        ev = ev + str(vars[el])
                    else:
                        ev = ev + str(el)
                varv = eval(ev)
                vars.update({varn : varv})
            elif (varv.startswith('"') and varv.endswith('"')):
                varv=  varv.replace('"' , " ")
                varv = varv.strip()
                vars.update({varn : varv})
            elif varv.startswith("'") and varv.endswith("'"):
                varv=  varv.replace("'" , "")
                varv = varv.strip()
                vars.update({varn : varv})
            elif not (varv.startswith('"') and varv.endswith('"')) or (varv.startswith("'") and varv.endswith("'")) :
                if varv.isdigit() == True:
                    varv = int(varv)
                    vars.update({varn : varv})
                varv = str(varv)
                if "." in varv:
                    varv = float(varv)
                    vars.update({varn : varv})
            else:
                raise Exception("Code[er01] Missing - ' ")
        
def spl_type(vn):
    tv = vars[vn]
    if type(tv) == int:
        print("type: int")
    elif type(tv) == str:
        print("type: str")
    elif type(tv) == float:
        print("type: float")

def spl_intconvert(vn):
    vv = vars[vn]
    if type(vv) == int:
        raise Exception("Code[er05] ; You cannot convert the int type of int")
    if vv.isdigit():
        vv = int(vv)
        vars.update({vn : vv})
    else:
        raise Exception("Code[er04] ; This value cannot be converted to a numeric data type")

def spl_strconvert(vn):
    vv = vars[vn]
    if type(vv) == str:
        raise Exception("Code[er06] -You cannot convert the str type of str ")
    vv = str(vv)
    vars.update({vn : vv})

def spl_floatconvert(vn):
    vv = vars[vn]
    if type(vv) == float:
        raise Exception("Code[er06] -You cannot convert the float type of float ")
    if type(vv) == int:
        vv = float(vv)
        vars.update({vn : vv})
    if type(vv) == str:
        if vv.isdigit() == True:
            vv = float(vv)
            vars.update({vn : vv})
        elif vv in digits and "." in vv:
                vv = float(vv)
                vars.update({vn : vv})
def main():
    os.system("cls")
    print("SPL Code v0.0.1 ")
    while True:
        try:
            interpriter()
        except Exception as e:
           print(f"Error; Code and Description - {e}")

if __name__ == "__main__":
    main()
else:
    raise Exception("Error ; SPL Code should not be imported into another program as a library")