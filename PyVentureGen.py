#This will generate a text based adventure template python script for you to plug your story into
#I started making a text based adventure and decided to make a framework for it
#By Philip Bove
#Contributions Aidan Noll
#
def start():
	main()

def main():
	usrsel = input('What would you like to do? \n help or adventure? > ') #First prompt
	if usrsel == 'adventure':
		gen()
	elif usrsel == 'help':
		print('my help text') #info and stuff here. will probably have it read a txt file
	else:
		print('unrecognized input') # y tho
		start()
def gen():# generate adventure file
	file = input('File name? > ')
	if '.py' not in file: #checks if .py file extension is already in file name
		file = file + '.py'
	numofsect = input('How many sections do you want? > ')
	num = 0
	with open(file,'w+') as f:
		f.write("""
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
	#Break this into seperate append function so user can come back and add to program
	#def append():
	count = 0
	while num < int(numofsect): #will take number of sections and spit out modularized code (I hope)
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
		num = num + 1
		count = count +1 #per repitition adds value to the ouput code for ease of working in it.
	f.write('''
start() ''')
	f.close
	print("Your file name is "+ file +" This program is complete.")		
	
	
start()