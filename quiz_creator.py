# Quiz Creator
#Create a function that asks user input to generate a question
def make_question():
    pass
#Create a function that writes the question in a text file
def make_file():
    pass
#Create a function that asks user to continue or not
def ask_continue():
    while True:
	ans = input("Would you like to continue? [Y/N]: ")
	if ans == "Y":
	    return True
	    break
	elif ans == "N":
	    return False
	    break
	else:
	    print("Invalid input. Please try again.")
#Call the functions to run the program
