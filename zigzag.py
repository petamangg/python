#hello guys today we are going to make a zigzag pattern using python!
import time , sys
indent = 0 # How many spaces to indent.
indentIncreasing = True #weather the indent is increasing or not

try:
    while True:  # this is going to be the main program loop
        print(' ' * indent, end='')
        print("*********")
        time.sleep(0.1) #pause for 1/10 of a second
        
        if indentIncreasing:
            #increase the number of spaces :
            indent = indent + 1 
            if indent == 10:
                #change direction
                indentIncreasing = False
        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change the direction : 
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
