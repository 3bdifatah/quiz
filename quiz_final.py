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
        'Which planet spins in the opposite direction to all the others in the solar system?': 'venus',
        'How many moons does Mars have?': '2'
    },
    'sports': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'simone biles',
        # The technically correct answer here is "Simone Biles", spelling her name with uppercase letters. Similar for Chicago, Brazil etc. 
        # It's better to store the correct form of the answer. If you want to allow answers in any case, 
        # convert the correct answer and user answer to lowercase and compare. 
        # Words can have different meanings with different capitalizations https://en.wikipedia.org/wiki/Capitonym  
        # and a quiz may wish to be strict about answers in the correct case. 
        # Having the correct answer stored in the correct case also looks better when you display the correct answer to the user. 
        'Which country has won the soccer world cup the most times?': 'brazil',
        'What does MLB stand for?': 'major league baseball'
    }
}

message = 'Thank you for playing. Goodbye'   # this could be moved to the main function - is it used anywhere else in the program?
# otherwise, if you have a number of strings displayed to the user, maybe move them all here as global variables. 
# The advantage of doing that, would make it easier to translate your program into another language, you can see all of the 
# text that needs to be created. 

# Use single quotes everywhere for string text in your program everywhere - or double quotes everywhere - 
# it doesn't matter which one, but be consistent. 


def main():
    while True:   
        try:
            topic = menu() # calls menu function and returns user input

            # for valid inputs
            # Would it be better to use the menu function to make sure that the user
            # has chosen a valid topic? 
            if topic == 'art' or topic == 'space' or topic =='sports':
                result= quiz(topic)   # if topic is 'art' or 'space' or 'sports' it must be lowercase
                feedback(result, len(questions[topic]))
                
                response= input('Play again? y/n: ').lower()   # asks user whether they want to play again
                if (response == 'no') or (response == 'n'):
                    print(message)
                    break

            elif topic == '':
                print(message)
                break

            # for invalid inputs
            else:
                print('please enter a valid input')
        except KeyError as e:
            print(e)  # How are you getting a key error? 
            # This is an error you can completely prevent by checking if the key is in the dictionary before trying to read it. 

def menu():  # can you use a more specific name for this function? Something like display_menu_get_user_choice() ? 
    """
    # menu function lists different topics and returns users choice
    """
    
    # Can you make this more general - what if a "history" or a "geology" topic was added to questions? 
    # What about looping over the keys in the questions dictionary and using that to print the topic choices?
    #
    # for topic in questions:
    #   print(topic)
    print('''
    art
    space
    sport
    enter to exit
    ''')
    topic = input('Please choose a topic: ')
    # This would be a better place to validate that the user has chosen one of the valid topics
    # You can check that the topic entered is one of the keys in the questions dictionary,
    # for example,   if topic in questions.keys():  is True if the topic is a dictionary key. 
    return topic.lower()



def quiz(topic):
    """
    quiz function takes the users topic and checks asks the questions in the dictionary for the topic.
    it also checks the user answer and keeps count how many are correct if not tells the user the correct answer.
    it returns the number of questions user got correct.
    """
    total_score = 0

    #gets the keys and values as question and answer
    for question, answer in questions[topic].items():
        print(question)
        user_answer = input()  # be consistent with spacing around operators - one space before and after
        
        # checks whether user answer matches the answers on the dictionary
        if user_answer.lower() == answer:
            print('correct!!')
            total_score += 1
        else:
            print(f'incorrect! the correct answer is {answer}')

    return total_score



def feedback(result, number_questions):
    """
    feedback function takes the number of questions user got correct and the total number of questions
    in the dictionary and displays the results 
    """
    if result == number_questions:
        print(f'awesome you got all of them correct!!! {result} out of {number_questions}')
    else:
        print(f'you got {result} out of {number_questions}')


if __name__ == '__main__':
    main()
