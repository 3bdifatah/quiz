"""
this program ask users questions based on the topic they choose then tells them wether they got it right 
or wrong. it also tracks the number of correct answers and tells them the correct answer if they get it wrong.
"""

# question dictionary stores 3 topics with 3 questions and answers
questions = {
    'art': {
        'Who painted the Mona Lisa?' : 'vincent van gogh',
        'What precious stone is used to make the artist\'s pigment ultramarine?': 'lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'chicago'    
    },
    'space': {
        'Which planet is closest to the sun?': 'mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
        'How many moons does Mars have?': '2'
    },
    'sports': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'Simone Biles',
        'Which country has won the soccer world cup the most times?': 'brazil',
        'What does MLB stand for?': 'Major League Baseball'
    }
}

message = "Thank you for playing. Goodbye"


def main():
    while True:   
        try:
            topic= menu() #calls menu function and returns user input

            # for valid inputs
            if topic == 'art' or topic == 'space' or topic =='sports':
                result= quiz(topic.lower())
                feedback(result, len(questions[topic.lower()]))
                
                response= input('Play again? y/n: ').lower()   #asks user wether they wanna play again
                if (response == 'no') or (response == 'n'):
                    print(message)
                    break

            elif topic == '':
                print(message)
                break

            #for invalid inputs
            else:
                print('please enter a valid input')
        except KeyError as e:
            print(e)

# menu function lists different topics and returns users choice
def menu():
    print('''
    art
    space
    sport
    enter to exist
    ''')
    topic= input('Please choose a topic: ')
    return topic.lower()


'''
quiz function takes the users topic and checks asks the questions in the dictionary for the topic.
it also checks the user answer and keeps count how many are correct if not tells the user the correct answer.
it returns the number of questions user got correct.
'''
def quiz(topic):
    total_score= 0

    #gets the keys and values as question and answer
    for question, answer in questions[topic].items():
        print(question)
        user_answer= input()
        
        # checks wether user answer matches the answers on the dictionary
        if user_answer.lower() == answer:
            print('correct!!')
            total_score += 1
        else:
            print(f'incorrect! the correct answer is {answer}')

    return total_score


'''
feedback function takes the number of questions user got correct and the total number of questions
in the dictionary and displays the results 
'''
def feedback(result, number_questions):
    if result == number_questions:
        print(f'awesome you got all of them correct!!! {result} out of {number_questions}')
    else:
        print(f'you got {result} out of {number_questions}')


if __name__ == '__main__':
    main()
