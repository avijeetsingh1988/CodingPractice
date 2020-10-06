import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

"""https://simpleguics2pygame.readthedocs.io/en/latest/#installation 
Normally Pygame is installed automatically when you install SimpleGUICS2Pygame. 
But if it is failed then install it like this first.
pip install pygame==1.9.6 --upgrade --user"""

COMPUTER_SCORE=0
HUMAN_SCORE=0
human_choice=''
computer_choice=''

def number_to_choice(choice):
    dic1={0:'rock',1:'paper',2:'scissors'}
    return(dic1[choice])

def choice_to_number(number):
    dic2={'rock':0,'paper':1,'scissors':2}
    return(dic2[number])

'''
#TESTS#
assert number_to_choice(0)=='rock'
assert number_to_choice(1)=='paper'
assert number_to_choice(2)=='scissors'
assert choice_to_number('rock')==0
assert choice_to_number('paper')==1
assert choice_to_number('scissors')==2
print('YOUR CODE IS CORRECT')
'''

def random_computer_choice():
    list1=['rock','paper','scissors']
    return random.choice(list1)


def choice_result(computer_choice,human_choice):
    global COMPUTER_SCORE
    global HUMAN_SCORE
    if computer_choice=='rock' and human_choice=='rock':
        return ('Its a tie')
    elif computer_choice=='paper' and human_choice=='rock':
        COMPUTER_SCORE=COMPUTER_SCORE+1
    elif computer_choice=='scissors' and human_choice== 'rock':
        HUMAN_SCORE=HUMAN_SCORE+1
    elif computer_choice=='rock' and human_choice=='paper':
        HUMAN_SCORE=HUMAN_SCORE+1
    elif computer_choice=='paper' and human_choice== 'paper':
        return ('Its a tie')
    elif computer_choice=='scissors' and human_choice=='paper':
        COMPUTER_SCORE=COMPUTER_SCORE+1
    elif computer_choice=='rock' and human_choice== 'scissors':
        COMPUTER_SCORE=COMPUTER_SCORE+1
    elif computer_choice=='paper' and human_choice=='scissors':
        HUMAN_SCORE=HUMAN_SCORE+1
    elif computer_choice=='scissors' and human_choice== 'scissors':
        return ('Its a tie')

def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()
