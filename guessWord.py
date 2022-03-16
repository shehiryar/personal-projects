#Guess the word game developed by SHEHIRYAR SABIR KHAN 18040210


from os import system

import turtle

def title(): #function for the title of the game which is to be displayed in turtle
    
    title = turtle.Turtle()
    title.penup() #penup stops drawing so it can movve the pen without drawing
    title.goto(-170, 100) #goto take the turtle pen to the given coordinates
    title.pendown() #when the pen is in the desired location, pendown is used to to draw
    title.ht()
    title.write("Guess the word:", align = "center", font = ("Arial", 28, "italic"))
    turtle.bgcolor("yellow")#sets the background color to yellow
    title.ht()


def ambulance_front(): #function that draws the front of the ambulance with taf standing for turtle ambulance front
    taf = turtle.Turtle()
    taf.ht()
    taf.fillcolor('white')
    taf.begin_fill()
    taf.penup()
    taf.goto(180, 10)
    taf.pendown()
    for i in range(4):
        taf.forward(90)
        taf.right(90)
    taf.end_fill()
    taf.left(90)
    taf.penup()

def ambulance_back(): #function that draws the back of the ambulance with tab standing for turtle ambulance back
    tab = turtle.Turtle()
    tab.ht()
    tab.fillcolor('white')
    tab.begin_fill()
    tab.penup()
    tab.goto(180, -80)
    tab.pendown()
    tab.left(90)
    tab.forward(150)
    tab.left(90)
    tab.forward(250)
    tab.left(90)
    tab.forward(150)
    tab.left(90)
    tab.forward(250)
    tab.end_fill()

def front_wheel(): #function that draws the front wheel of the ambulance with tfw standing for turtle front wheel
    tfw = turtle.Turtle()
    tfw.ht()
    tfw.penup()
    tfw.goto(140, -90)
    tfw.forward(20)
    tfw.right(90)
    tfw.pendown()
    tfw.fillcolor('grey')
    tfw.begin_fill()
    tfw.circle(30)
    tfw.end_fill()

def back_wheel(): #function that draws the back wheel of the ambulance with tbw standing for turtle back wheel
    tbw = turtle.Turtle()
    tbw.ht()
    tbw.penup()
    tbw.goto(-40, -90)
    tbw.forward(20)
    tbw.right(90)
    tbw.pendown()
    tbw.fillcolor('grey')
    tbw.begin_fill()
    tbw.circle(30)
    tbw.end_fill()

def siren(): #function that draws the siren on the top of the ambulance with ts standing for turtle siren
    ts = turtle.Turtle()
    ts.ht()
    ts.penup()
    ts.begin_fill()
    ts.fillcolor('red')
    ts.goto(135,70)
    ts.pendown()
    ts.left(90)
    ts.forward(15)
    ts.right(90)
    ts.forward(15)
    ts.right(90)
    ts.forward(15)
    ts.right(90)
    ts.forward(15)
    ts.end_fill()

def cross1(): #function that draws the vertical bar of the cross on the ambulance with tc1 standing for turtle cross1
    tc1 = turtle.Turtle()
    tc1.ht()
    tc1.penup()
    tc1.goto(51,40)
    tc1.pencolor('red')
    tc1.pendown()
    tc1.begin_fill()
    tc1.fillcolor('red')
    tc1.forward(10)
    tc1.right(90)
    tc1.forward(45)
    tc1.right(90)
    tc1.forward(10)
    tc1.right(90)
    tc1.forward(45)
    tc1.right(90)
    tc1.end_fill()

def cross2(): #function that draws the horizontal bar of the cross on the ambulance with tc2 standing for turtle cross2
    tc2 = turtle.Turtle()
    tc2.ht()
    tc2.penup()
    tc2.goto(34,23)
    tc2.pencolor('red')
    tc2.pendown()
    tc2.begin_fill()
    tc2.fillcolor('red')
    tc2.forward(45)
    tc2.right(90)
    tc2.forward(10)
    tc2.right(90)
    tc2.forward(45)
    tc2.right(90)
    tc2.forward(10)
    tc2.right(90)
    tc2.end_fill()

def window(): #function that draws the window on the front of the ambulance with tw standing for turtle window
    tw = turtle.Turtle()
    tw.ht()
    tw.penup()
    tw.goto(200,-10)
    tw.pencolor('black')
    tw.pendown()
    tw.begin_fill()
    tw.fillcolor('light blue')
    tw.forward(30)
    tw.right(90)
    tw.forward(30)
    tw.right(90)
    tw.forward(30)
    tw.right(90)
    tw.forward(30)
    tw.right(90)
    tw.penup()
    tw.end_fill()

def tries_left(): #function that writes out on the turtle screen how many tries remain 
    draw = turtle.Turtle()
    draw.speed(0) 
    draw.pencolor("yellow")
    draw.penup()
    draw.goto(-100, -250)
    draw.pendown()
    draw.fillcolor("yellow")
    draw.begin_fill()
    draw.forward(50)
    draw.left(90)
    draw.forward(50)
    draw.left(90)
    draw.forward(50)
    draw.left(90)
    draw.forward(50)
    draw.end_fill()

def restart_game(): #function that asks the user if they would like to restart the program
    print("\n\n\n\nWould you like to play again?\n")
    reset = input("Yes/No\n") #asks the user if they would like to restart the game or not using a simple yes or no question
                    
    while True:
        if reset == 'Yes' or 'yes':
            print("Good luck with your next game!\n\n\n\n\n\n")
            turtle.clearscreen() #clears the turtle screen for the next game
            return main() #runs the whole game again

        elif reset == 'No' or 'no':
            print("-------------------------------------")
            print("**HOPE YOU ENJOYED PLAYING THE GAME**")
            print("-------------------------------------")
            break

        if reset != 'yes' or 'Yes' or 'no' or 'No':
            print("[!] Please only enter Yes or No")
            reset = input("Yes/No\n")

        elif reset == "":
            print("You cannot leave this blank, please enter Yes/No")
            reset = input("Yes/No\n")

        else:
            break                      
    

    
def show_correct_guesses(correct_guess): #function to fill out the missing spaces on the screen
    xPos = -150
    tscg = turtle.Turtle()
    tscg.penup

    tscg.goto(xPos, 180)
    tscg.write("Guess the word:" , font = ("Arial", 26, "normal"))

    tscg.goto(xPos, 180)
    for i in range (len(correct_guess)):
        tscg.write(right_guess[i], font = ("Arial", 26, "normal"))
        xPos = xPos + 20
        tscg.goto(xPos, 180)

def hide_word(player1_input): #function that hides the input given by player1
    tstar = turtle.Turtle()
    tstar.penup()
    tstar.goto(-150, 180)
    tstar.pendown()
    tstar.write(player1_input, font = ("Arial", 26, "normal"))

    
    
def main(): #the main function
    title()#shows the title of the game
    turtle.bgcolor("yellow") #sets the background color to yellow
    wordToBeGuessed = []
    player1_input = []
    correct_guess = []
    incorrect_guess = []
    
    totalTries = 8 #sets the number of total attempts to 8
    
    player1_input = "" #sets the player1 input to be empty



    print("-----------------------------")
    print("* WELCOME TO GUESS THE WORD *")
    print("-----------------------------")

  
    print("\n***** PLAYER 1 *****\n")

    
    wordToBeGuessed = input("Please input a word for Player 2 to guess(make sure Player 2 isn't looking)\n") #asks player 1 to enter a word for player 2 to be guessed

    while True:

        if wordToBeGuessed == "": #prevents the entry from being blank
            print ("[!] You can't leave it blank.\n")
            wordToBeGuessed = input("Please input a word for Player 2 to guess(make sure Player 2 isn't looking)\n")

        elif len(wordToBeGuessed) < 3: #prevents the entry from being less than 3 letters
            print("The entered word has to contain three or more letter. Try again./n")
            wordToBeGuessed = input("Please input a word for Player 2 to guess(make sure Player 2 isn't looking)\n")

        else:
            break

        

    while totalTries > 0: #a while loop that runs while the player still has an attempt or more remaining
        
        player1_input = "" #ensures player 1 enters a word
        for letter in wordToBeGuessed:
            if letter in correct_guess:
                player1_input = player1_input + letter
            elif letter not in correct_guess:
                player1_input = player1_input + "*"#reveals a star for the next letter to be guessed
                break


        if player1_input == wordToBeGuessed: #if both entries match, then the victory message is displayed on both screens
            win = turtle.Turtle()
            win.penup()
            win.goto(-320, 300)
            win.pendown()
            win.write("YOU GUESSED IT! YOU WIN!", font = ("Arial", 28, "bold"))
            print("The word player 1 made you guess was", wordToBeGuessed, "and you guessed it correctly, CONGRATULATIONS!")
            return restart_game() #runs the function which allows users the choice of restarting game         
            break

        
    
  
        print("\n***** PLAYER 2 *****\n")

        hide_word(player1_input)
        print("The hidden word has",len(wordToBeGuessed),"letters")#shows player 2 how many letters the hidden word has
        player2_input = input("Enter your guess: ")
        

        print(player1_input)
        
    
        if player2_input == "": #ensures guess isnt left blank
            print("[!] You cannot leave your guess blank.")
            player2_input = input("\nEnter your letter: ")
        elif len(player2_input) != 1: #ensures player 2 only guesses once at a time
            
            print("[!] You cannot enter multiple letters. Please enter one letter at a time.")
            player2_input = input("\nEnter your letter: ")
        
    
        if player2_input in correct_guess or player2_input in incorrect_guess:#checks if this entry has already been entered
            print("[!] You already guessed this letter", player2_input)
        elif player2_input in wordToBeGuessed:
            print("Good job, keep guessing.")
            correct_guess.append(player2_input)
            print("Your wrong guesses are: ", incorrect_guess)
        else:
            print("[!] This letter is not in the word.")
            totalTries = totalTries - 1 #decreases number of attempts left each time an incorrect guess is written
            print("You have", totalTries, "tries", "left")
            ttries = turtle.Turtle()
            ttries.ht() 
            ttries.penup()
            ttries.goto(-250, -250)
            ttries.write("Tries left:", font = ("Arial", 28, "normal"))

        if totalTries == 8:
            tries_left()
            t8 = turtle.Turtle()
            t8.ht() 
            t8.penup()
            t8.goto(-90, -250)
            t8.pendown()
            t8.write(totalTries, font = ("Arial", 28, "normal"))
            t8.penup()
            t8.goto(-250, -250)
            t8.write("Tries left:", font = ("Arial", 28, "normal"))
            
        
        elif totalTries == 7: #when total tries are 7, it shows up on screen and draws the front of the ambulance
            tries_left()
            t7 = turtle.Turtle()
            t7.ht() 
            t7.penup()
            t7.goto(-90, -250)
            t7.pendown()
            t7.write(totalTries, font = ("Arial", 28, "normal"))
            ambulance_front()
            
        elif totalTries == 6: #when total tries are 6, it shows up on screen and draws the back of the ambulance
            tries_left()
            t6 = turtle.Turtle()
            t6.ht() 
            t6.penup()
            t6.goto(-90, -250)
            t6.pendown()
            t6.write(totalTries, font = ("Arial", 28, "normal"))
            ambulance_back()
                     
        elif totalTries == 5:  #when total tries are 5, it shows up on screen and draws the front wheel of the ambulance        
            tries_left()
            t5 = turtle.Turtle()
            t5.ht() 
            t5.penup()
            t5.goto(-90, -250)
            t5.pendown()
            t5.write(totalTries, font = ("Arial", 28, "normal"))
            front_wheel()
            
        elif totalTries == 4:    #when total tries are 4, it shows up on screen and draws the back wheel of the ambulance           
            tries_left()
            t4 = turtle.Turtle()
            t4.ht() 
            t4.penup()
            t4.goto(-90, -250)
            t4.pendown()
            t4.write(totalTries, font = ("Arial", 28, "normal"))
            back_wheel()
            
        elif totalTries == 3:  #when total tries are 3, it shows up on screen and draws the siren of the ambulance         
            tries_left()
            turtle_3 = turtle.Turtle()
            turtle_3.ht() 
            turtle_3.penup()
            turtle_3.goto(-90, -250)
            turtle_3.pendown()
            turtle_3.write(totalTries, font = ("Arial", 28, "normal"))
            siren()
            
        elif totalTries == 2:    #when total tries are 2, it shows up on screen and draws the window on the front of the ambulance        
            tries_left()
            t2 = turtle.Turtle()
            t2.ht()
            t2.penup()
            t2.goto(-90, -250)
            t2.pendown()
            t2.write(totalTries, font = ("Arial", 28, "normal"))
            window()
            
        elif totalTries == 1:  #when total tries are 1, it shows up on screen and draws the first part of the cross on the back of the ambulance
            tries_left()
            t1 = turtle.Turtle()
            t1.ht()
            t1.penup()
            t1.goto(-90, -250)
            t1.pendown()
            t1.write(totalTries, font = ("Arial", 28, "normal"))
            cross1()
            
        elif totalTries == 0:  #when total tries are 0, it shows up on screen and draws the second part of the cross on the back of the ambulance
            tries_left()
            t0 = turtle.Turtle()
            t0.ht()
            t0.penup()
            t0.goto(-90, -250)
            t0.pendown()
            t0.write(totalTries, font = ("Arial", 28, "normal"))
            cross2()
            tt = turtle.Turtle()
            tt.penup()
            tt.goto(0, 130)
            tt.pendown()
            tt.ht()
            tt.penup()
            tt.write("You lost!", font = ("Arial", 30, "italic"))
            tt.ht()
            return restart_game()
        
        
        
main()                            
                      
