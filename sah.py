import sys
try:
    assert sys.argv[1]
except:
    exit()
import sah_lexer as lexer
import sah_parser as parser
import time
if sys.argv[1] == '-i':
    print("SAH - 2022\nDeveloped by Just_a_Mango and Anousk")
elif sys.argv[1]:
    def readprocess(filename):
        with open(filename,"r") as code:
            for line in code.readlines():
                print("DEBUG => "+str(parser.parse(lexer.lexing(line))))
    time_i = time.time_ns() / (10 ** 9)
    readprocess(sys.argv[1])
    time_f = time.time_ns() / (10 ** 9)
    difference = time_f - time_i
    print("\33[92mRun time (including print): \33[34m"+str(difference)+"\33[0m")