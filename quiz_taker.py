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

    for line in contents:
        line = line.strip()
        if line.startswith("Question"):
            questions.append(line.removeprefix("Question: "))
        elif line.startswith("a", "b", "c", "d"):
            each_choices.append(line)
            if len(each_choices) == 4:
                choices.append(each_choices)
                each_choices == []
        elif line.startswith("Answer"):
            correct_answers.append(line.removeprefix("Answer: "))

#Create a function that randomizes the questions
def randomize_quiz(question, choice, answer, number):
    random_order = []
    while True:
        random_num = random.randint(0, len(question))
        if random_num not in random_order:
            random_order.append(random_num)
            if len(random_order) == len(question):
                break
            
#Create a function that welcomes the user to start and how many items to quiz

#Call the functions to run the program
