###############################
# SPL | Simple program language
###############################
import time
import os 
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)
digits = "123456789"
vars = {}
constant = {"PI" : 3.14159 , "E" : 2.71828 , "PHI" : 1.618}
erline = None
def spl_sumstr(a : list):
    rl = ""
    for el in a:
        if (el.startswith('"') and el.endswith('"')) or (el.startswith("'") and el.endswith("'")):
            rl = rl + el
        else:
            raise Exception(Fore.RED + "Сode [er08] ; Adding a string with a number")
        if el in vars.keys():
                ti = vars[el]
                if type(ti) == str:
                    rl = rl + '"' + vars[el] + '"'
                else:
                    raise Exception(Fore.RED + "Сode [er08] ; Adding a string with a number")
    rt = eval(rl)
    return rt

def compiler(f , iml : str):
    start = time.time()
    readfunc = ""
    erline = 0
    if not (".spl" in f):
        raise Exception(Fore.RED + "File ; ", f , "Code[er07] ; The file does not meet the requirements. Missing '.spl' in the file name")
    if iml != "lib":
        os.system("cls")
        print("SPL Code v0.0.3\nCompiling from file: " , f)
    file = open(f , "r" , encoding="utf-8")
    fileread = file.read()
    filesp = fileread.split("\n")
    for line in filesp:
        erline += 1
        line = line.strip()
        if line.startswith("#"):
            continue
        elif line.strip() == "":
            continue
        else:
            if "(" in line and ")" in line:
                comline = line.replace(")" , "")
                comlinesp = comline.split("(")
                func = comlinesp[0]
                if func == "print":
                    args = comlinesp[1].strip()
                    argslist = args.split(",")
                    printer(argslist)
                elif func == "read":
                    commentf = comlinesp[1].strip()
                    spl_input(commentf)
                elif func == "delv":
                    delarg = comlinesp[1]
                    delarg = delarg.split(",")
                    for x in delarg:
                        if x in vars.keys():
                            del vars[x]
                        else:
                            raise Exception(Fore.RED + f"[er13] ; Line {erline} ; - You have requested the deletion of a non-existent variable")
                elif func == "use":
                    libop = comlinesp[1].strip()
                    compiler(libop , "lib")
                elif func == "constlist":
                    for k,v in constant.items():
                        print( k , ":" , v , ";" )
                    
                else:
                    raise Exception(Fore.RED + f"Code[er03] ; Line : {erline}  - Invalid syntax")
            elif line.startswith("const"):
                line = line.replace("const" , "" , 1)
                line = line.strip()
                constlist = line.split("=")
                constn = constlist[0].strip()
                constv = constlist[1].strip()
                if constn in constant.keys():
                    raise Exception(Fore.RED + f"Code [er14] Line: {erline} You cannot change constants")
                constant.update({constn : constv})
            elif "=" in line:
                linesp = line.split("=")
                varn = linesp[0].strip()
                varval = linesp[1].strip()
                if varval.startswith("read"):
                    varval = varval.replace(")" , "")
                    varvalrsp = varval.split("(")
                    readfunc = varvalrsp[0].strip()
                    argcommentfile = varvalrsp[1].strip()
                    line = line.replace(")" , "")
                    line = line.replace("(" , "")
                if varval.startswith("sumstr"):
                    varval = varval.replace(")" , "")
                    varvalsssp = varval.split("(")
                    readfunc = varvalsssp[0].strip()
                    liststrsum = varvalsssp[1].strip()
                    liststrsum = liststrsum.split("+")
                    for i in range(len(liststrsum)):
                        liststrsum[i] = liststrsum[i].strip()
                    line = line.replace(")" , "")
                    line = line.replace("(" , "")
                if varn[0].isdigit():
                    raise Exception(Fore.RED + f"Code[er02] ; Line : {erline} - A variable cannot start with a number ")
                if varn in constant.keys():
                    raise Exception(Fore.RED + f"Code [er14] Line: {erline} You cannot change constants")
                else:
                    if readfunc == "read":
                        r_val = spl_input(argcommentfile)
                        vars.update({varn : r_val})
                        readfunc = ""
                    elif readfunc == "sumstr":
                        rvn = spl_sumstr(liststrsum)
                        vars.update({varn : rvn})
                        readfunc = ""
                    elif varval in vars.keys():
                        varval = vars[varval]
                        vars.update({varn : varval})
                    elif '+' in varval or "-" in varval or "/" in varval or '*' in varval or "**" in varval or "//" in varval or "%":
                        ev = ""
                        prel = ""
                        if "*" in varval:
                            tms = varval.split("*")
                            if len(tms) == 2:
                                st  = tms[0].strip()
                                if (st.startswith('"') and st.endswith('"')) or (st.startswith('"') and st.endswith('"')) :
                                    inm = tms[1].strip()
                                    if st in vars.keys():
                                        st = vars[st]
                                    if inm in vars.keys():
                                        inm = vars[inm]
                                    ev = st + "*" + inm
                        for el in constant.keys():
                            if el in varval:
                                varval = varval.replace(el,  str(constant[el]))
                        for el in vars.keys():
                            if el in varval:
                                varval = varval.replace(el, str(vars[el]))
                        comlistfile = list(varval)
                        comlistfile = [w for w in comlistfile if w.strip()]
                        for el in comlistfile:
                                ev = ev + str(el)
                        varv = eval(ev)
                        vars.update({varn : varv})
                    elif(varval.startswith('"') and varval.endswith('"')):
                        varval=  varval.replace('"' , "")
                        varval = str(varval)
                        varval = varval.strip()
                        vars.update({varn : varval})
                    elif (varval.startswith("'") and varval.endswith("'")):
                        varval=  varval.replace('"', "")
                        varval = str(varval)
                        varval = varval.strip()
                        vars.update({varn : varval})
                    elif not (varval.startswith('"') and varval.endswith('"')) or (varval.startswith("'") and varval.endswith("'")) :
                        if varval.isdigit() == True:
                            varval = int(varval)
                            vars.update({varn : varval})
                        elif "." in varval:
                            varval = float(varval)
                            vars.update({varn : varval}) 
                    else:
                        raise Exception(Fore.RED + f"Code[er01]; Line : {erline} Missing - ' ")                  
            else:
                raise Exception(Fore.RED + f"Code[er03] ; Line : {erline}  - Invalid syntax")
    if iml != "lib":
        print()
        finish = time.time()
        print(Fore.LIGHTGREEN_EX + f"Process finished. Time spent: {finish - start}")
def printer(arlis : list):
    if arlis[0] == "":
        print()
    else:
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
                    elif x in constant.keys():
                        tot = tot + str(constant[x]) + " "
                    else:
                        raise Exception(Fore.RED + f"Code[er01] ; Line : {erline} Missing - ' ")
            print(tot)

def spl_input(k=""):
    if k != "":
        if not (k.startswith('"') and k.endswith('"')) or (k.startswith("'") and k.endswith("'")):
            raise Exception(Fore.RED + "Code[er01] Missing - ' ")
        elif k.startswith('"') and k.endswith('"'):
            k = k.replace('"', "")
        elif (k.startswith("'") and k.endswith("'")):
            k = k.replace("'", "")
    user_input = input(k)
    return user_input

        
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
        raise Exception(Fore.RED + "Code[er05] ; You cannot convert the int type of int")
    if vv.isdigit():
        vv = int(vv)
        vars.update({vn : vv})
    else:
        raise Exception(Fore.RED + "Code[er04] ; This value cannot be converted to a numeric data type")

def spl_strconvert(vn):
    vv = vars[vn]
    if type(vv) == str:
        raise Exception(Fore.RED + "Code[er06] -You cannot convert the str type of str ")
    vv = str(vv)
    vars.update({vn : vv})

def spl_floatconvert(vn):
    vv = vars[vn]
    if type(vv) == float:
        raise Exception(Fore.RED + "Code[er06] -You cannot convert the float type of float ")
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
    print("SPL Code v0.0.3")
    while True:
        try:
            com = input(" >> ")
            if "(" in com and ")" in com:
                com = com.replace(")", "")
                com = com.split("(" )
                if len(com) == 2:
                    func = com[0].strip()
                    arg = com[1].strip()
                    match func:
                        case "open":
                            compiler(arg , "nolib")
                else:
                     raise Exception(Fore.RED + "Code[er03] ; Invalid syntax")
                    
        except Exception as e:
           print(Fore.RED + Style.BRIGHT +f"Error; Code and Description - {e}")
        except FileNotFoundError:
            print(Fore.RED + f"Error ; File not found")

if __name__ == "__main__":
    main()
else:
    raise Exception("Error [IMPER01]; SPL Code should not be imported into another program as a library")