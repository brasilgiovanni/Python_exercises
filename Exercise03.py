# Looping with FOR and While
def startgame():
	start = input('''Hey there! would u like to start? 
			YES? or NO?
	 .........................................			''' )
	if start == 'YES' or 'Yes' or 'yes':
		word = input('Entre com uma palavra:' )
		while word != 'exit':
			for letter in word:
				print(letter)
			print('please! writing the word "exit" to go out')		
	return "thanks by gaming with us"
startgame()