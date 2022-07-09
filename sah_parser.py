import os
import time
variables = []

def error(message):
    print("\33[91m" + message + "\33[0m")

def concat(a, b):
    if isinstance(a, str) == True and isinstance(b, str) == True:
        return a + b
    elif isinstance(a, int) == True and isinstance(b, int) == True:
        return a + b
    elif isinstance(a, float) == True and isinstance(b, float) == True:
        return a + b
    else:
        error("Cannot concatenate "+str(type(a))+" and "+str(type(b)))


def parse(tokens=["print","PARENT_START","STR(d)", "ADD", "STR(e)", "STR(5)", "ADD", "STR(6)", "PARENT_END"]):
    if "ADD" in tokens:
        final_index = []
        final_value = ""
        for x in range(tokens.count("ADD")):
            print("AddIndex(s): "+str([i for i, n in enumerate(tokens) if n == 'ADD']))
            addIndex = [i for i, n in enumerate(tokens) if n == 'ADD'][x]
            concatenated = concat(tokens[addIndex-1], tokens[addIndex+1])
            tokens[addIndex] = tokens[addIndex].replace(tokens[addIndex], concatenated)
            final_index.append(addIndex)
            tokens.pop(addIndex+1)
            tokens.pop(addIndex-1)
        for x in final_index:
            final_value = concat(str(final_value),str(tokens[x]))
        print("VALUE"+final_value)
        
    elif "GIVES" == tokens[1]:
        variables.append((tokens[0], tokens[2],"str"))
    elif "print" == tokens[0]:
        for x in range(tokens.count("PARENT_START")):
            for content in tokens[[i for i, n in enumerate(tokens) if n == 'PARENT_START'][x]+1 : [i for i, n in enumerate(tokens) if n == 'PARENT_END'][x]]:
                if "STR(" in content:
                    print(content.replace("STR(", "").replace(")", ""))
                elif not "STR(" in content:
                    print([item for item in variables if item[0] == content][0][1])
                    
 
                    
                    
                    
    return tokens

parse()