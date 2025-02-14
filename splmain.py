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
        elif (x.startswith('"') and x.endswith('"' )):
            x =  x.replace('"' , " ")
            x = str(x)
            tot = tot + x + " "
        elif (x.startswith("'") and x.endswith("'")):
            x =  x.replace("'" , " ")
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

def interpriter():
    global func, com
    com = input(" >> ")
    cr_var()
    if "(" in com and ")" in com:
        com = com.replace(")" , "")
        comsp = com.split("(")
        func = comsp[0]
        func = func.strip()
        if func == "print":
            args = comsp[1].split(",")
            printer(args)
        elif func == "delv":
            args = comsp[1].split(",")
            for el in args:
                del vars[el]
        else:
            raise("Code[er003] - Invalid comand")
        
def cr_var():
    global com
    if "=" in com:
        comsp = com.split("=")
        varn = comsp[0].strip()
        varv = comsp[1].strip()
        if varn[0] in digits:
            raise Exception("Code[er02] ; A variable cannot start with a number ")
        else:
            if varv in vars.keys():
                varv = vars[varv]
                vars.update({varn : varv})
            elif '+' in varv or "-" in varv or "/" in varv or '*' in varv or "**" in varv:
                comli = list(varv)
                comli = [w for w in comli if w.strip()]
                ev = ""
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
                varv=  varv.replace("'" , " ")
                varv = varv.strip()
                vars.update({varn : varv})
            elif not (varv.startswith('"') and varv.endswith('"')) or (varv.startswith("'") and varv.endswith("'")) :
                if varv.isdigit() == True:
                    varv = int(varv)
                    vars.update({varn : varv})
                else:
                    raise Exception("Code[er01] Missing - ' ")
        
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