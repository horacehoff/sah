import re

def lexing(input):
    is_brackets = False
    final = ""
    to_remove = []
    index = 0
    for c in input:
        if c in '"':
            if is_brackets == False:
                is_brackets = True
            else:
                is_brackets = False
            final = final + c
        else:
            if is_brackets == False:
                if c in "{":
                    final = final + " BRACK_START "
                elif c in "}":
                    final = final + " BRACK_END "
                elif c in "(":
                    final = final + " PARENT_START "
                elif c in ")":
                    final = final + " PARENT_END "
                elif c in "T" and input[index+1] == "r" and input[index+2] == "u" and input[index+3] == "e":
                    to_remove.append(index+1)
                    to_remove.append(index+2)
                    to_remove.append(index+3)
                    final = final + " BOOL(TRUE) "
                elif c in "F" and input[index+1] == "a" and input[index+2] == "l" and input[index+3] == "s" and input[index+4] == "e":
                    final = final + " BOOL(FALSE) "
                    to_remove.append(index+1)
                    to_remove.append(index+2)
                    to_remove.append(index+3)
                    to_remove.append(index+4)
                elif c in "+":
                    final = final + " ADD "
                elif c in "=" and input[index+1] == "=":
                    final = final + " EQUAL "
                    to_remove.append(index+1)
                elif c in "=":
                    final = final + " GIVES "
                elif c in "/":
                    final = final + " DIVIDE "
                elif c in "*":
                    final = final + " MULTIPLY "
                else:
                    if index not in to_remove:
                        final = final + c
            elif index not in to_remove:
                    final = final + c 
        index += 1
    # Replacing all the strings in the final with STR(string)
    match = re.findall('"(.*?)"', final)
    for strings in match:
        final = final.replace(strings, " STR(" + strings + ") ")
    final = final.replace('"','')
    final = ' '.join(final.split())+" "
    nb_brackets=0
    final = final.strip(" ") # get rid of leading/trailing seps

    l=[0]
    for i,c in enumerate(final):
        if c=="(":
            nb_brackets+=1
        elif c==")":
            nb_brackets-=1
        elif c==" " and nb_brackets==0:
            l.append(i)
        # Handle string that are not well formed
        if nb_brackets<0:
            raise Exception("Syntax error")

    l.append(len(final))
    # Handle unclosed parentheses
    if nb_brackets>0:
        raise Exception("Syntax error")


    final= [final[i:j].strip(" ") for i,j in zip(l,l[1:])]
    return final