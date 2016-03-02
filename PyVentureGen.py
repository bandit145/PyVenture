#This will generate a text based adventure template python script for you to plug your story into
#I started making a text based adventure and decided to make a framework for it
#By Philip Bove
#Contributions Aidan Noll and Mike Hall
#TO DO: PRETTY UP CONVENTIONS AND CODE! 2/29/2016 -Bove
#       MOVE THINGS OVER TO A MORE CLASS/METHOD BASED SYSTEM 2/29/2016
#       MAKE ACTUAL GAME CODE BETTER AND MORE MODULAR 2/29/2016
################################################################
#Variable List:
#main func:
#   usrsel is for determining what the user wants to do
#maininput func:
#   file holds the file name the user selects in maininput (This is passed through the rest of the functions)
#   numofsect holds the number of repeating sections that the user wants(This is passed to the rest of the functions
#  appendinput:
#   appendfile holds the file name of the file to be appended
#   appendsect holds the number of repeating sections that the user wants added (Both are passed through to the new functions)
#gen func:
#   basecontent contains the PY_BASE variable from Class01 of the class file (Which has the base "game" code
#append func:
#   f contains the imported returnf mathod from the class file(which takes file name from append and spits it back to be used by thr f.write)
################################################################
from PyVentureClass import*
def start():
    main()

def main():
    usrsel = input('What would you like to do? \n help, adventure or append? > ') #First prompt
    if usrsel.lower() == 'adventure':
        maininput()
    elif usrsel.lower() == 'append': #need to pass file name to append
        appendinput()
    elif usrsel.lower() == 'help':
        print('my help text') #info and stuff here. will probably have it read a txt file
    else:
        print('unrecognized input') # y tho
        start()
#handles input for gen
def maininput():
    file = input('File name? > ')
    if '.py' not in file: #checks if .py file extension is already in file name
        file = file + '.py'
    numofsect = input('How many sections do you want? > ')
    gen(numofsect,file)
#This function handles input for append
def appendinput():
    appendfile = input('File name? > ') #Goes into append function
    appendsect = input('How many sections do you want? > ')
    if '.py' not in appendfile: #checks if .py file extension is already in file name
        appendfile = appendfile + '.py'
    append(appendsect,appendfile)
#gen generates a new file with the primer code and then moves to append
def gen(numofsect,file):
    basecontent = Class01.PY_BASE
    with open(file,'w+') as f:
        f.write(basecontent)
    append(numofsect,file,)
#append appends an already created file
def append(numofsect,file,):
    returnf = Class01.returnf
    writeto = Class01.appendmeth
    num = 0
    count = 0
    while num < int(numofsect): #will take number of sections and spit out modularized code (I hope)
        writeto(Class01,file,count)
        num = num + 1
        count = count +1 #per repitition adds value to the ouput code for ease of working in it.
    f = returnf(Class01,file)
    f.write('''
start() ''')
    f.close
    print("Your file name is "+ file +" This program is complete.")


start()