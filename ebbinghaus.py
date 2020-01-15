import json
import random
with open ('tests/state_capitals.json', 'r') as f:
    test = json.load(f)
    question=test['question']
    q_and_a = test['q_and_a']
    # print(q_and_a)
    while True == True:
        i = random.randint(0,len(q_and_a) - 1)
        answer = input(question + q_and_a[i][0] + '? ')
        if answer == 'quit':
            break
        elif answer ==  q_and_a[i][1]:
            print('\nCorrect!\n')
        else:
            print('\nSorry. The answer is ' + q_and_a[i][1] + '.\n')
# TODO
# Change color on question, anwer and response, right and wrong
# Add read file for questions and answers
# Give option to choose a topic
# Add spaced learning
# Suggest topics based on spaced learning
# Allow for timed answers and overall time of quiz
# Allow for rverse questions
# Add to github
# Add reamde
# Add to git
# Add multiple chiosce
# Create tests from wikipedia or other sources
# Fill in the blank
