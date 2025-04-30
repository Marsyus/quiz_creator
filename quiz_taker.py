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

#Create a funtion to randomize the order of the questions
def randomize_order(count):
    random_order = []
    while True:
        random_num = random.randint(0, count - 1)
        if random_num not in random_order:
            random_order.append(random_num)
            if len(random_order) == count:
                return random_order

#Create a function that displays the questions
def generate_quiz(question, choice, answer, number, order):
    item = order[number]
    print(f"{number + 1}. {question[item]}")
    for each in choice[item]:
        print("  " + each)
    while True:
        valid_choices = ("a", "b", "c", "d")
        user_ans = input("\nEnter your answer [a/b/c/d]: ")
        if user_ans in valid_choices:
            if user_ans == answer[item]:
                print("\nYou are correct!")
                return 1
            else:
                print("\nSorry, you are incorrect!")
                return 0
        else:
            print("\nInvalid input. Please try again.")

#Create a function that welcomes the user to start and how many items to quiz
def start_quiz(count):
    while True:
        try:
            num = int(input(f"There are {count} questions available. How many would you like to answer? : "))
            if count >= num >= 0:
                return num
            else:
                print("\nInvalid input. Please try again.\n")
        except:
            print("\nInvalid input. Please try again.\n")

#Create a scoring system
def score(points, max_points):
    if points == max_points:
        return "Congrats! You perfectly passed the quiz!"
    elif max_points > points >= max_points / 2:
        return "Congrats! You passed the quiz!"
    elif max_points / 2 > points >= 0:
        return "You did not pass the quiz. Better luck next time!"

#Call the functions to run the program
quiz = read_file("quiz.txt")
count = len(quiz[0])
item_count = start_quiz(count)
random_order = randomize_order(count)
points = 0
for num in range(item_count):
    print("\n===========")
    print(f"Score: {points}/{item_count}")
    print("===========\n")
    points += generate_quiz(*quiz, num, random_order)

print(f"You scored {points}/{item_count}", score(points, item_count))
