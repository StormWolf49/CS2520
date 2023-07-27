#Name: Nikhil Kowdle
#Lab 8
#This program contains the tasks required for this assignment.

try :
    retval = ""
    check = False
    myFile = open(input("Please enter the filename: "), "r")
    check = True
    namelist = []
    datalist = []
    for line in myFile :
        print(line, end='')
        values = line.split()
        namelist.append(values[0])
        try :
            datalist.append(float(values[1]))
        except ValueError :
            print("Value not a float, will be replaced by 0.0")
            datalist.append(0.0)
            retval = "File not fomatted correctly, no calculations done."
        print()
        #note: after split, each element is a string
        #to use numeric values, need type conversion
except FileNotFoundError :
    retval = "File not found, program ending"
except : #catch-all handler
    retval = "An unkown error has occured"
else :
    print("sup")
    #no wrong data items nor other errors, so calculate the highest etc.
finally :
    if check :
        print(namelist)
        print(datalist)
        myFile.close()
    print(retval)
    #close the file
    #you may print out additional messages or perform other actions in any step of above. 
