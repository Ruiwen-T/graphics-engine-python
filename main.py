from script import run
import sys

if len(sys.argv) == 2:
    run("mdl_files/" + sys.argv[1])
elif len(sys.argv) == 1:
    # provided code is incorrect
    #run(raw_input("please enter the filename of an mdl script file: \n"))
    raise IndexError("Too few arguments.")
else:
    raise IndexError("Too many arguments.")
