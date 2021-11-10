import requests
import pprint
import json
import random
import html
url = "https://opentdb.com/api.php?amount=1&category=18"
endGame = ""
score_correct = 0
score_incorrect = 0
while endGame != "quit":
    valid_answer = False
    r = requests.get(url)
    if r.status_code != 200:
       endGame = input("Sorry, There was a problem retrieving the question, Press enter to try again or 'quit' to quit")
    else:
        answer_number = 0
        date = json.loads(r.text)
        question = date["results"][0]['question']
        answers = date["results"][0]['incorrect_answers']
        correct_answer = date["results"][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print(html.unescape(question) + "\n")
        for answer in answers:
            answer_number = answer_number + 1
            print(answer_number,': ' + html.unescape(answer))

        while valid_answer == False:
            try:
                user_answer = input("Type the number of correct question : ")
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalide answer !")
                else:
                    valid_answer = True
            except:
                print("Invalid answer, Use only numbers !")

        if correct_answer == answers[user_answer-1]:
            score_correct += 1
            print("Congratulations, You answer correctly, The correct answer was : ", html.unescape(correct_answer))

        else:
            score_incorrect += 1
            print("Sorry, ", html.unescape(answers[user_answer-1]), "is incorrectly", "The correct answer was : ", html.unescape(correct_answer))

        print("*******************************")
        print("Your score is : ")
        print("Correct answer(s) : " + str(score_correct))
        print("Incorrect answer(s) : " + str(score_incorrect))
        print("*******************************")

        endGame = input("Press enter to try again or 'quit' to quit ").lower()


print("\n Thanks for playing :D ")






