import time
import random
import sys
import os
name = 'Stranger'


#Clears the screen
def clear_screen():
  # if windows 
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def bad_end_game_screen():

    clear_screen()

    print("""
               -|-
                |
            .-'~~~`-.
          .'         `.
          |  R  I  P  |
          |           |
          |           |
        \\|           |//
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  """)
    print("You are real Bad Luck Brian\n")

    print("- I've not witnessed someone perform so poorly in quizzes and riddles since the last run of 'Who Wants to be a Millionaire'.\n")
    time.sleep(3)
    print("- I could not in my right mind entrust thee with the reward that it would be the recipe to the cure for COVID-19.\n")
    time.sleep(3)
    print("- If there art other mortals roaming the earth only as intelligent as thou, then it might be best leaving them to perish.\n")
    time.sleep(3)
    print("- As we promised from the start, 'it's either victory or death' and as it stands - thou hast ended up in the latter.\n ")
    time.sleep(2)
    print("YOU DIED") #cheeky Dark Souls reference
    
    time.sleep(1)
    sys.exit(1)



def cave_matt():

    clear_screen()
    
    '''
      Random factor in the game.
      Calls random number from 1 to 10
      if its 7 it takes you to bad_end_game_screen
    '''
    if random.randint(0,10) == 7:
      bad_end_game_screen()

    print("""\n
                              .--.                 
          ::\`--._,'.::.`._.--'/::     
          ::::.  ` __::__ '  .::::  <----Yoda  
          ::::::-:.`'..`'.:-::::::
          ::::::::\ `--' /:::::::: )
 \n
          """)

    print("""
          You came into spacious cave, with walls covered in moss.
          In the middle of your path there is a little green man with long pointy ears.
          And he says....
    """)
    
    print(f"\nJudge me by my size, do you {name}?")

    print("\nFear is the path to the dark side…fear leads to anger…anger leads to hate…hate leads to suffering.\n")
    
    riddles = [ 
      ["Give me food, and I will live. Give me water, and I will die. What am I?\n", ["Water", "Sand", "Air", "Fire"], "fire"],
      [" What has to be broken before you can use it?\n",["Glass","Egg","Plate","Car"],"egg"],
      ["What gets wet while drying?\n",["Hands", "Sink", 'Towel', 'Dishes'],"towel"],
    ]

    for riddle in riddles:
      print("Riddle me this!\n")
      time.sleep(1)
      print(riddle[0])
      print("What is your answer?\n")
      time.sleep(1)
      while True:
          answer = input(f"{'/'.join(riddle[1])} ")
          if answer.lower() == riddle[2]:
            print('Well done!')
            print('Always pass on what you have learned\n')
            break
          else:
            print('Wrong answer')
            print('Happens to every guy sometimes this does\n')


def cave_ricardo():

    clear_screen()

    riddle = "- What is always in front of you, but cannot be seen?\n"
    answers = "future", "the future"
    print("After walking, and eventually dragging your feet for what felt like an eternity, you finally come to a break in the pattern\n.")
    time.sleep(3)
    print("You realize that you are inside a peculiar-looking cave. In a way, it felt like it was attend to often.\n")
    time.sleep(3)
    print("Almost as if to make it hospitable.\n")
    time.sleep(3)
    print("Suddenly, a man appears. Seemingly materialized out of thin air and says:\n")
    time.sleep(3)
    print("- I am going to keep it short as I have no time to waste here, mortal. Riddle me this:\n")
    time.sleep(3)
    print(riddle)
    time.sleep(2)
    answer = input("What is your answer? > \n")
    if answer.casefold() in answers:
        print("- Big brain! You shall advance.\n")
        time.sleep(2)
        input("Are you ready to continue?[Enter any key to continue]")
    else:
        print("- YOU FOOL! Come back here when you reach 200 points of IQ.\n")
        start_game()


def cave_marcin():

    clear_screen()

    time.sleep(1)
    print("You're tired. You've been walking for the past two days, looking for another cave. After passing your test at the previous cave, you blacked out. You don't know how long you've been asleep for. You can't keep up long l ike this. but wait, you see something, a cave?\n")
    time.sleep(1)
    print("It's pitch black, you can't see anything. You're moving forwards, reaching out with your hands to feel a wall, object, anything.. Unexpectedly, your hand meets an object. It feels weird, something.. \n")
    time.sleep(2)
    print("Then, you can feel the object moving out of your hand, room enlightens and you see a Sphinx, standing in front of you in all its glory.\n")
    time.sleep(1)
    print("You're trying to ask a question but you can't get any words out. You're speechless.\n")
    time.sleep(1)
    print(f"Sphinx:\n I know what you're looking for, {name}. The only way to pass through onto the next challenge is by answering my simple riddle.\n")
    time.sleep(1)

    print("You're terrified. You suck at riddles and it's the only way to survive now.\n")
    print("F O C U S \n")
    time.sleep(0.1)

    print("Sphinx:\n What walks on four legs in the morning, two legs in the afternoon, three legs in the evening, and no legs at night?\n")
    time.sleep(1)
    user_answer1 = input("What or who is it? >>>> \n")
    time.sleep(1)
    
    # user_answer3 = input("What or who is it? >>>> \n")
    # solution = "a man" or "man"

    if user_answer1 == "a man" or user_answer1 == "man" or user_answer1 == "human" or user_answer1 == "a human" or user_answer1 == "Human" or user_answer == "Man":
        print("\nWell done.")
        time.sleep(1)
        print("Next riddle. ")
        time.sleep(1)
        print("\nSphinx:\n As I was going to St. Ives,\n I met a man with seven wives,\n Each wife had seven sacks,\n Each sack had seven cats,\n Each cat had seven kits:\n Kits, cats, sacks, and wives,\n")
        time.sleep(1)
        user_answer2 = input("How many were there going to St. Ives? >>>> \n")
        print("\nNow you can move further. Last riddle.\n")
        time.sleep(2)
        
    else:
        print("You answered wrong. You shall die. ")
        bad_end_game_screen()

    if user_answer2 == "one":
      print("\nSphinx:\nThis thing all things devours;\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel;\nGrinds hard stones to meal;\nSlays king, ruins town, \nAnd beats mountain down.")
      time.sleep(1)
      user_answer3 = input("\nWhat is it? >>>> \n")
      time.sleep(2)
      input("\nAre you ready to continue?[Enter any key to continue]")
    else:
      bad_end_game_screen()
    
    if user_answer3 == "time":
      print("Well done. You can move further. Good luck. ")
      time.sleep(2)
    else:
      bad_end_game_screen()


def cave_daniel():

    clear_screen()

    print("You light your torch and move further into the cave...\n")
    time.sleep(1)
    print("You move through dark and eerie passages until you come upon a great stone door...\n")
    time.sleep(1)
    print("Examining the door you notice some writing, it reads: 'Oi mate, I can't talk but I can reply... What am I?\n")
    time.sleep(1)
    print("To open the door you must answer correctly...\n")
    time.sleep(1)
    answer = input("What is your answer?\n")
    # solution = "echo" or "Echo" or "an echo" or "An echo"
    if answer == "echo" or answer == "Echo" or answer == "an echo" or answer == "An echo":
        print("The stone begins to shake and crumble... You fall back as the great stone doors slowley open...\n")
        time.sleep(1)
        print("Looking up you see the now open entrance, deeper into the cave... You stand up, dust yourself off and move forward...\n")
        time.sleep(2)
        input("Are you ready to continue?[Enter any key to continue]\n")
    else:
        print("You answer but nothing happens... you fool\n")
        start_game()


def cave_ryan():

  clear_screen()

  print("Making your way down your chosen path you take a look around noticing that this cave is very cave like made out of stone and everything!\n")
  time.sleep(2)
  print("This is your reality without a phone, I know, it's a horrible thing to experience.\n")
  time.sleep(2)
  print("As you continue on your path you finally see some light coming through, the excitment is so overwhelming you start running towards what you believe is the exit.\n")
  time.sleep(2)
  print("Getting closer to the exit you reailise to late that running inside a cave was one of the worst decisions you could have possible made as you trip careening through the air at a breakneck pace closing your eyes in antisipation for the inevitable collision with the floor.\n")
  time.sleep(5)
  print("You realise that you have been falling for alot longer than you should have been, opening your eyes you stunned by what you see.\n")
  time.sleep(3)
  print("You're no longer falling!... you think, taking a look at your surroundings you apear to be in the outside world once more, but you're floating? In the sky? You look around and see the only source of light illuminating your surrounding. It looks like the moon is so close you feel like you could reach out your hand and...\n")
  time.sleep(2)
  print("You grabbed the moon... holding it in your hands you take a second to try and piece together what the hell is going on, but before you can, you hear a voice.\n")
  time.sleep(2)
  print(f"greetings {name} I see you wish to leave this place.\n")
  time.sleep(2)
  print("\"What the fuck?\" you think to yourself\n")
  time.sleep(2)
  answer = input(
        "To leave you must answer 3 trivia questions, are you ready? [Yes/No]")
  if answer.lower() == "yes" or 'y':
    print("Excellent.\n")
    answer = input("In the movie The Lord Of The Rings: The Two Towers, did the actor who played aragorn break his toes on set [yes/no]\n")
    if answer.lower() == "yes":
      print("Correct the actor indeed broke 2 of his toes during the scene in which they believe they have found the remains of 2 of the hobbits.")
      time.sleep(2)
      answer = input("What is the most recent album from gorillaz?\n")
      if answer.lower() == "song machine":
        print("Correct, this is the final question if you get this wrong you die :D\n")
        time.sleep(2)
        answer = input("What's was the name of king Arthur's sword?\n")
        if answer.lower() == "excalibur":
          print("Whoa... you really know your stuff, huh. You may pass on to the next  area whenever you're ready.")
          time.sleep(4)
          input("Are you ready to continue?[Enter any key to continue]")
        else:
          print("You were so close. That's really too bad, I was rooting for you as well... you really let me down, how could you do this to me, you absolute monster. This isn't how the story is suppose to end... NOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!.\n")
          time.sleep(2)
          answer = input("Start again? [Yes]")
          if answer.lower() == "yes":
            print("Thank you for trying again")
            
          elif answer.lower() == "no":
            print("you done fucked up my dude.")
            time.sleep(2)
          else:
            print("You fool you think you had a Choice!!!!!")
            time.sleep(2)
            start_game()
      else:
        print(f"incorrect you no longer exist goodbye {name}")
        answer = input("start again? [Yes]")
        if answer.lower() == "yes":
          print("Thank you for trying again")
          start_game()
        else:
          print("Too bad XD")
          time.sleep(1)
          start_game()
    elif answer.lower() == "no":
        print("I see.")
        time.sleep(2)
        print("You didn't realise what they meant by that until the moon shined the purest white you have ever seen and... you ceased to exist.")
        time.sleep(2)
        print("Game over")
        answer = input("Start again? [Yes]")
        if answer.lower() == "yes":
            print("Thank you for trying again")
            start_game()
        else:
            print("Too bad XD")
            time.sleep(1)
            start_game()
  else:
    print("That's the wrong answer dumb dumb.")
    start_game()


def end_game_screen():

    clear_screen()

    print("""
                           ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                           \|               :::::/|/
                            |               ::::::|
                            | Special Flonk Award:|
                            |    for Silliness::::|
                            |               ::::::|
                            |              .::::::|
                            J              :::::::F
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
____________________________________|     |_________________________________________
                                    |  :::|
                                    F   ::J
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `\"\"\"---------\"\"\"\'
    """)

    print(f"\n\n- Congratulations {name} , oh traveler - surveyor and prospector of caves! As thy presence here proves that thou art indeed worthy of holding the answers to life itself,\n thou shan't remain ignorant to the mysteries of modern medicine either!")
    time.sleep(8)  # NOTE: long message, so I added a lot more sleep time.
    print("\n- Now BEHOLD! Our gift to thee!")
    time.sleep(1)
    print("\nYou have acquired a Legendary item!")
    time.sleep(2)
    print("x1 'COVID-19 Cure Recipe' was added to your inventory!\n")
    time.sleep(1)
    
    again = input("\nWould you like to play again?[yes/no]\n")

    if again.lower() == 'yes' or 'y':
      start_opening()
    else:
       print("Now go, good luck with future challenges. And if we shall see each other again, my hope is that thou won't need to wear a mask.")
       time.sleep(2)
       sys.exit(0)



# List of available caves
cave_list = [cave_matt, cave_daniel, cave_ricardo, cave_marcin, cave_ryan]


# This function randomize cave order
# when list is empty returns end_game_screen
def display_caves_in_random():
    random.shuffle(cave_list) #NOTE shuffles the list
    # goes through the list and calls functions
    for fn in cave_list:
        fn()

def start_game():

    clear_screen()

    print(f"When you first open your eyes {name}")
    time.sleep(2)
    print("You notice you're in a dimly lit cave with only one exit so you start to walk down it cause what else is there to do.\n")
    time.sleep(2)
    print("As you start to travel down this cave the more you realise how much you actualy hate caves\n")
    time.sleep(2)
    print("The further you travel down this cave the more questions you have like \"Why the FUCK am I in a cave how the hell did this happen?\" but as you continue walking you realise that that dosen't matter right now the only thing that matters is getting the hell out of here.\n")
    time.sleep(4)
    print("Walking through this pitch black cave isn't the best idea you've ever had why didn't you have your phone with you when you woke up in a cave? the same reason you woke up in a cave...\n")
    time.sleep(4)
    print("Plot convenience\n")
    time.sleep(3)
    print("By now your feet are starting to hurt and frustaration is setting in but then you feel somthing, a warm breeze is flowing through the cave \"this must be the way out\" you think to yourself as you start moving towards the exit.\n")
    time.sleep(4)
    print("As you reach the exit your eyes slowly start ajusting to the light and the first thing that you see is an orb hovering in the sky as bright as the sun itself.\n")
    time.sleep(3)
    print("The next thing you see is...")
    
    
    # time.sleep(2)
    # name = input("What is your name? ")
    
    time.sleep(1)
    response = input("Are you sure you'd like to proceed? [Y/N] ")
    if response == "Y" or response == "y" or response == "Yes" or response == "yes":
      time.sleep(1)
      cave_daniel()
      cave_marcin()
      cave_matt()
      cave_ricardo()
      cave_ryan()

    elif response == "N" or response == "n" or response == "No" or response == "no":
      print("Fine, be that way.")
      time.sleep(1)
      print("Good luck and goodbye.")
      bad_end_game_screen()
    else:
      print("Are you sure you don't want your COVID cure? Think again. ")
      time.sleep(1)
# This is where the game starts

def start_opening():

    clear_screen()

    print("""
                  _________________
             ____/#################\____
         ___/################,##########\___
       _/################/##/ \##\##########\_
      /#################/\##| |##/\###########\\
     /##################\ \#| |#/ /############\\
    |##DWB###############\ \| |/ /#########JRB##|
    |####################{{{\ /}}}##############|
    |###################{{<.> <.>}}#############|
    |#####################{ | | }###############|
    |#####################{ | | }####_#######__#|
    |#####################/_| |_\##_( )###__(  )_
    |####################{(_)_(_)}(  ` )_( '__ ` )
    |#####################{VV_VV}##(__( `)_(  )-` )
    |#####################\^^))^/######(   )_')  )
    |######################--((-########( ' _)__)
    |########################))##########(__)###|
    |########################(##################|
    |###########################################|
    |###########################################|
    |###########################################|
    |###########################################|
\ | /########| |################################| \ | /
_\|/|#######/   \####################\|/########|__\|/___
            \   /
             \ /
              V
    """)

    print("Hello and welcome to 'Riddle-cure'.")
    print("You are entering the riddle caves in the quest for COVID-19 Cure.")
    print("It's either win or death.\n")
    print("In order to win, you must answer all the questions correctly.")
    print("There's no room for mistakes.")
    print("There's no points... ")
    print("One mistake can cost you .. life. ")
    print("If you answer correctly, and then wrong, you die. If you answer wrong off the bat - YOU  D I E")
    print("Are you ready?")
    
    # name = input("What is your name? ")
    # if name == '':
    #     name = 'Stranger'
    # elif name == 'Jay':
    #     print('Are you sure about that mate? Oh well')

    # time.sleep(1)
    # print(f"Hello {name}!\n")
    time.sleep(1)
    response = input("Are you sure you'd like to proceed? [Y/N] ")
    
    if response.lower() == "y" or response == "yes":
        print("Let's go!")
        global name
        name = input("Enter your name >>> ")
        if name == '':
          name = 'Stranger'
        elif name.lower() == 'jay':
          print('Are you sure about that mate?')
          time.sleep(2)
          print('...100% sure?')
          time.sleep(1)
    
        start_game()
        end_game_screen()
    elif response.lower() == "n" or response == "no":
        print("Fine, be that way.")
        time.sleep(1)
        print("Good luck with rona and goodbye.")
    else:
        print("Are you sure you don't want your COVID cure? Think again. ")
        time.sleep(1)

start_opening()
# cave_matt()


