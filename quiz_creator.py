# Quiz Creator
#Create a function that asks user input to generate a question
def make_question():
    question = "Question: "
    question += input(f"Enter your question: ")
    a, b, c, d = "a.) ", "b.) ", "c.) ", "d.) "
    a += input(f"Enter choice for letter a: ")
    b += input(f"Enter choice for letter b: ")
    c += input(f"Enter choice for letter c: ")
    d += input(f"Enter choice for letter d: ")
    choices = ["a", "b", "c", "d"]
    while True:
        ans = input("Choose a correct answer [a/b/c/d]: ").lower()
        if ans in choices:
            answer = "Answer: " + ans
            break
        else:
            print("Invalid input. Please try again.")
    return question, a, b, c, d, answer
#Create a function that writes the question in a text file
def make_file(item):
    for text in item:
        file = open("quiz.txt", "a")
        file.write(f"{text}\n")
        file.close()
#Create a function that asks user to continue or not
def ask_continue():
    while True:
        ans = input("Would you like to continue? [Y/N]: ").upper()
        if ans == "Y":
            return True
        elif ans == "N":
            return False
        else:
            print("Invalid input. Please try again.")
#Call the functions to run the program
while True:
    quiz = make_question()
    make_file(quiz)
    if ask_continue():
        continue
    else:
        break
