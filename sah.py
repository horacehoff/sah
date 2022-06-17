import sah_lexer as lexer
import datetime

def readfile(filename):
    with open(filename,"r") as code:
        for line in code.readlines():
            print(lexer.lexing(line))
            
first_time = datetime.datetime.now()
readfile("tets.sah")
later_time = datetime.datetime.now()
difference = later_time - first_time
print(difference.total_seconds())