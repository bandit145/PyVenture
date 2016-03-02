class Class01: # class file for PyVentureGen
    #Did this because classes are cool and declutter the program like a b0ss
    #PY_BASE is for the gen function in the main program. I need to actually work on the game code itself soon - 3/2/2016 Bove
    PY_BASE = ("""
#PyVenture by Philip Bove|
#Created on 2/8/2016     |
#                        |
# This is to start you along your journy of making text based cmd line adventures|
# Just run this and start                                                        |
#------------------------|
def start(): #my beginning function
    basegame()
def basegame():
    inventory = {} #dict pls
    choices = ['choice0', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5'] #choices, will probably expand
    print ('output')
    selection = input('> ' )
    if selection == choices[0]:
        print('stuff here') #sectioning game into functions, all choices will call a new function segment at some point
        choice0(inventory)
    elif selection == choices[1]:
        print('output')
    elif selection == choices[2]:
        print('output')
    elif selection == choices[3]:
        print('output')
    elif selection == choices[4]:
        print('output')
    elif selection == choices[5]:
        print('output.')
    else: """#break this into seperate end(): function to be called whenever you die?
    """
        print('output')
        restart = input('Would you like to continue? y/n > ')
        if restart == 'y':
            start()
        elif restart == 'n':
            print('See you next time!')

                """)
    # appendmeth is for appending already created files.
    def appendmeth(self,file,count):
        f = open(file,"a")
        f.write("""

def choice"""+str(count)+"""(inventory"""+str(count)+"""):
    choices"""+str(count)+""" = ['choice0','choice1','choice2','choice3','choice4','choice5'] #Enter choices user choices here
    Sel"""+str(count)+""" = input( 'put prompt here')
    if sel"""+str(count)+"""  == choices"""+str(count)+"""[0]:
        print('stuff here') #sectioning game into functions, all choices will call a new function segment at some point
        choice0()
    elif sel"""+str(count)+"""  == choices"""+str(count)+"""[1]:
        print('output')
    elif sel"""+str(count)+""" == choices"""+str(count)+"""[2]:
        print('output')
    elif sel"""+str(count)+""" == choices"""+str(count)+"""[3]:
        print('output')
    elif sel"""+str(count)+""" == choices"""+str(count)+"""[4]:
        print('output')
    elif sel"""+str(count)+""" == choices"""+str(count)+"""[5]:
        print('output.')
    else:
        print('no recognized input') #loop back?
            """)#Write the the code thing here
    #Returnf makes f= to whatever it needs to be and return it so the main program can append the file again.
    def returnf(self,file):
        f = open(file,"a")
        return f



