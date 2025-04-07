# Quiz Creator
#Create a function that asks user input to generate a question
def make_question(num):
    question = f"{num}. "
    question += input(f"Enter your question: ")
    a, b, c, d = "a.) ", "b.) ", "c.) ", "d.) "
    a += input(f"Enter choice for letter a: ")
    b += input(f"Enter choice for letter b: ")
    c += input(f"Enter choice for letter c: ")
    d += input(f"Enter choice for letter d: ")
    choices = ["a", "b", "c", "d"]
    while True:
	answer = input("Choose a correct answer [a/b/c/d]: ")
	if answer in choices:
	    break
	else:
	    print("Invalid input. Please try again.")
    return question, a, b, c, d, answer
#Create a function that writes the question in a text file
def make_file(item):
    for text in item:
	file = open("/storage/emulated/0/quiz.txt", "a")
	file.write(f"{text}\n")
#Create a function that asks user to continue or not
def ask_continue():
    while True:
	ans = input("Would you like to continue? [Y/N]: ").upper()
	if ans == "Y":
	    return True
	    break
	elif ans == "N":
	    return False
	    break
	else:
	    print("Invalid input. Please try again.")
#Call the functions to run the program
count = 1
while True:
    quiz = make_question(count)
    make_file(quiz)
    if ask_continue():
        count += 1
    else:
        break
