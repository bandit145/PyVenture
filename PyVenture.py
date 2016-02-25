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
	inventory = []
	print ('output')
	selection = input('> ' )
	if selection == choices[0]:
		print('stuff here') #sectioning game into functions, all choices will call a new function segment at some point
		choice0()
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
	else:
		print('output')
			restart = input('Would you like to continue? y/n > ')
			if restart == 'y'
				start()
			elif restart == 'n'
				print('See you next time!')
				break

def choice():
	choices = ['choice0','choice1','choice2','choice3','choice4','choice5'] #Enter choices user choices here
	Sel = input( 'put prompt here')
	if selection == choices[0]:
		print('stuff here') #sectioning game into functions, all choices will call a new function segment at some point
		choice0()
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
	else:
		print('no recognized input') #loop back?
		
	
			
		
	
	