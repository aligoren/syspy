from sys import exit

def play():
	print("\nSysPy Windows! Exit('q, quit, exit')")
	print("\nasd\n")
	while True:
		c_input = input(">> ")
		if c_input == 'xyz':
			print('hihi')
		elif c_input == 'x':
			print('haha')
		elif c_input == 'q' or c_input == 'quit' or c_input == 'exit':
			print("\nGoodbye!")
			exit(1)

play()