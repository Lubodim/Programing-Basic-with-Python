import random

right_answer = 0
bad_answer = 0

print("*********************************************************************************")

print("*******************************      Hello !!!     ******************************")

print("*********************  This is the  MINUTE IS TOO MUCH  Game  *******************")

print("*********************************************************************************")
print("*********************************************************************************")
print("*********************************************************************************")
print("************************     This game was created by     ***********************")
print("*********************************************************************************")
print("*****************************    Lyubomir Dimitrov    ***************************")
print("*********************************************************************************")
print()

print(f"Please write your name here: ", end="")
name = input()

print(f"{name} are you ready to proof your self")

my_list = ["Question from Physics", "Question from Chemistry", "Question from History", "Question from Mathematics"]
physics_question = [1, 2, 3]
chemistry_question = [4, 5]
history_question = [6, 7]
mathematics_question = [8, 9]

dictionary_answers = {1: (1.0, 1.1, 1.2, 1.3), 2: (2.0, 2.1, 2.2, 2.3), 3: (3.0, 3.1, 3.2, 3.3),
                      4: (4.0, 4.1, 4.2, 4.3), 5: (5.0, 5.1, 5.2, 5.3), 6: (6.0, 6.1, 6.2, 6.3),
                      7: (7.0, 7.1, 7.2, 7.3), 8: (8.0, 8.1, 8.2, 8.3), 9: (9.0, 9.1, 9.2, 9.3)}
dictionary_right_answer = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0, 8: 8.0, 9: 9.0}
while True:
    status = input(f"YES or NO \n").upper()
    if status == "NO":
        print("Good Bye")
        break
    if status != "NO" and status != "YES":
        print(f"You must choice 'Yes' or 'NO', try again")
        continue
    elif status == "YES":
        while True:
            current_list = random.choice(my_list)
            current_question = ""
            if current_list == "Question from Physics":
                current_question = random.choice(physics_question)
            elif current_list == "Question from Chemistry":
                current_question = random.choice(chemistry_question)
            elif current_list == "Question from History":
                current_question = random.choice(history_question)
            elif current_list == "Question from Mathematics":
                current_question = random.choice(mathematics_question)
            print(f"{current_list}: {current_question}")
            print()
            index = 0

            for ans in (dictionary_answers[current_question]):
                print(f"{chr(97 + index)}) {ans}")
                index += 1
                print()
            answer = input("Yor answer is: \n")
            
print()
