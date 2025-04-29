# Quiz Taker
#Import random
import random

#Create a function that reads a text file that contains questions generated from 'quiz_creator.py'
def read_file(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    
    questions = []
    choices = []
    each_choices = []
    correct_answers = []
    valid = ("a", "b", "c", "d")

    for line in contents:
        line = line.strip()
        if line.startswith("Question"):
            questions.append(line.removeprefix("Question: "))
        elif line.startswith(valid):
            each_choices.append(line)
            if len(each_choices) == 4:
                choices.append(each_choices)
                each_choices = []
        elif line.startswith("Answer"):
            correct_answers.append(line.removeprefix("Answer: "))

    return questions, choices, correct_answers

#Create a function that randomizes the questions
def randomize_quiz(question, choice, answer, number):
    random_order = []
    while True:
        random_num = random.randint(0, len(question) - 1)
        if random_num not in random_order:
            random_order.append(random_num)
            if len(random_order) == len(question):
                break
    
    item = random_order[number]
    print(f"{number + 1}. {question[item]}")
    for each in choice[item]:
        print(each)
    while True:
        valid_choices = ("a", "b", "c", "d")
        user_ans = input("Enter your answer [a/b/c/d]: ")
        if user_ans in valid_choices:
            if user_ans == answer[item]:
                print("You are correct!")
            else:
                print("Sorry, you are incorrect!")
            break
        else:
            print("Invalid input. Please try again.")

#Create a function that welcomes the user to start and how many items to quiz
def start_quiz(count):
    while True:
        try:
            num = int(input(f"There are {count} questions available. How many would you like to answer?"))
            if count >= num >= 0:
                return num
            else:
                print("Invalid input. Please try again.")
        except:
            print("Invalid input. Please try again.")

#Call the functions to run the program
quiz = read_file("quiz.txt")
count = len(quiz[0])
item_count = start_quiz(count)
for num in range(item_count):
    randomize_quiz(*quiz, num)
