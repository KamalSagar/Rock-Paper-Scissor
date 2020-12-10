'''this is a Rock Paper Scissor game'''
import time, random
print("  ***W-E-L-C-O-M-E***")
time.sleep(1)
print("        TO         ")
time.sleep(1)
print("ROCK PAPER SCISSOR GAME")
time.sleep(1)
game=['r', 'p', 's']

print("       enter  ")
print("     r for Rock    ")
print("     p for Paper    ")
print("     s for Scissor    ")
print("You have only 3 chances.")

win=0
loose=0
# print(game)
chance=0
while(chance<3):
    choice=random.choice(game)
    player=input().lower()
    if(player=="r" and choice=="r"):
        print("This match is draw")

    elif player=="r" and choice=="p":
        print("YOU LOOSE")
        chance+=1
        loose+=1
            
    elif player=="p" and choice=="r":
        print("YOU WIN")
        chance+=1
        win+=1
        
    elif player=="p" and choice=="s":
        print("YOU LOOSE")
        chance+=1   
        loose+=1
        
    elif player=="s" and choice=="p":
        print("YOU WIN")
        chance+=1
        win+=1
        
    elif player=="p" and choice=="p":
        print("DRAW")
        
    elif player=="r" and choice=="s":
        print("YOU WIN")
        chance+=1 
        win+=1  
         
    elif player=="s" and choice=="s":
        print("draw")
        
    elif player=="s" and choice=="r":
        print("YOU LOOSE")
        chance+=1
        loose+=1
        
    else:
        print("Invalid entry!")
         
if loose>win:
    print("GAME OVER\n")
if loose<win:
    print("You won the match\n")              
print(f"\nYou win {win} times.\nComputer win {loose} time")
print("Thank you for playing this game.")
    
