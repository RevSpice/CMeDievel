import random
import time
#I'll get back to this later...
print("CMeDievel v 1.0")
print("")
print("")                   
mountains='''                       
  ^^^^    ^^^    **   **    |[_0_] 
 ^    ^ ^ ***^^ **** ****   |[ 
^      ^  ***  ^ ||   ||    |[   '''


opened_gates='''              
  ^^^^    ^^^    **   **    '[_0_] 
 ^    ^ ^ ***^^ **** **** '  [
^      ^  ***  ^ ||   || ----['''
spooky_goblin='''#####
#0#0#
##0##'''

castle='''
|[___]----------[___]
|[   ]        H     ]   
|[            0     ]'''




spooky_bat='''>0-0<'''

day1="You, a lonely %s, decide to leave your cozy life and set out on an adventure. Only time will tell what the future holds..."
day4="You grow nervous, having not seen any being in 3 days"
XP=0
instructions="Press x to move, d to attack. Do not worry about capitalization. Press I to view stats"         

print("PRESS X TO START")
road=''''''
distance="."
counter=0
marker="day %s"

class Goblin:
    def __init__(self,health,attack):
        self.health=health
        self.attack=attack
class Bat(Goblin):
    pass
class Player:
    def __init__(self,health,attack,weapon):
        self.health=health
        self.attack=attack
        self.weapon=weapon

Player=Player(5,1,"dagger")
Goblin=Goblin(4,1)
Bat=Bat(3,2)

A="Goblins health is %s"
B="Your health is %s"
at="Players attack is %s"
avatar=input("Type a personalised avatar here. Only one line. Be creative.")


while True:
    input1=input("")
    if input1=="I" or input1=="i":
        print(instructions)
    if input1=="x" or input1=="X":
        counter=counter+1
        if counter<=20:
            
            print(marker % counter)
            print(mountains)
        if counter>20:
            print("Next level, you'll see a spoky castle")
            print(castle)
            break
            
            
            print(opened_gates)
        if counter>25:
            import hello
            break
            #thats all for now
            

        
        print((distance*counter)+avatar)
        if counter==1:
            print(day1 % avatar)
        elif counter==4:
            print(day4)

        if Player.health<=0:
            print("ayy better luck next time")
            break
     
            
        
        print(road)
        
        if counter==5:
            print("A Super Spooky Goblin jumped out! He is super hostile! You need to attack!")
            print(spooky_goblin)
            while Goblin.health>0:
                
                input2=input("d to attack")
                if input2=="d" or input2=="D":
                    attack_noises=["Swish!","Stab!","boop."]
                    choice=random.choice(attack_noises)
                    print(choice)
                    if choice=="Swish!" or choice=="Stab!":
                        Goblin.health=Goblin.health-2
                        print(A % Goblin.health)
                    if choice=="boop.":
                        print("The goblin laughs at you. He also bites you.")
                        Player.health=Player.health-1
                    if Player.health==0:
                        print("you lost")
                        break
                        print(B % Player.health)
                    if Goblin.health==0:
                        print("YOU WIN THE FIGHT")
                        print("Level up! +2 Health")
                        Player.health=Player.health+2
                        print(B % Player.health)
                        print("press x to continue")
        if counter==8:
            print("The excitement has worn off from your first adventure. Perhaps there will be something else in store...")

        if counter==10:
            print("you see a really frightening 6 asteriks cave.")
              
            print("You have found a new weapon. A staff! +3 Attack")
            Player.weapon="Staff"
            Player.attack=Player.attack+3
            print(at % Player.attack)
            print("")
            print("Unfortunately though, a bat jumps out at you. It tries to bite your throat, but its teeth are too soft from bad oral hygine")
            print(spooky_bat)
            print("")
            print("Truely horrifying isnt it")
            while Bat.health>0:
                i=input("d to attack, as always. r to run away")
                if i=="d" or i=="D":
                    attack_noises=["Swing!","Thrash!","poke."]
                    choice=random.choice(attack_noises)
                    print(choice)
                    if choice=="Swing!" or choice=="Thrash!":
                        dmg=Player.attack
                        if dmg>Bat.health:
                                print("annilated! You have won the battle")
                                print("X to move forward")
                                break
                    if choice=="poke.":
                                print("You poke one of the bat's horribly rotten teeth. It is less than amused")
                if i=="r" or i=="R":
                    sits=["You trip over a rock on the way out. You lose a health, but you make it out alive","You escape cleanly","You are paralyzed in fear"]
                    a=random.choice(sits)
                    if a==sits[0]:
                        Player.health=Player.health-1
                        print(a)
                        print('')
                        print(B % Player.health)
                        print("x to continue, as always")
                        break
                    elif a==sits[1]:
                        print(a)
                        print("")
                        break
                    else:
                        print(sits[2])

        if counter==15:
            print("Unlike yourself 9 days ago, you have come to enjoy the silence, for you know it will not last long")
        if counter==20:
            print("HALT! WHO GOES THERE!")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("uhhhh me?")
            time.sleep(1)
            print("YES YOU!!! This is the kingdom of Lounging, turn around!")
            time.sleep(3)
            print("uhhh, I hate to say this, but I can't really turn around")
            time.sleep(3)
            print("I have no free will")
            time.sleep(3)
            print("I only exist to do whatever the controller wants me to do, within what the source code allows")
            time.sleep(3)
            print("Besides, by the rules of the game, I can't turn back")
            time.sleep(3)
            print("I have to keep going forward")
            time.sleep(3)
            print("...")
            time.sleep(5)
            print("Just like in real life...")
            time.sleep(2)
            print("I.. I..")
            time.sleep(3)
            print("I was almost going to laugh at you and turn you down, that dramatic pause really did it for me. You  may come to our kingdom")
            time.sleep(4)
            print("Woohoo!")
            print(opened_gates)
            


                        
                        
            
            

    
    
                
            
            
            


