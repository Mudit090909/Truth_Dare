import random 

def name_of_the_players(number_of_players):
    global players
    players=[]
    for i in range(1,number_of_players+1):
        players.append(input(f"Enter the name of Player {i}: "))
        
def game():
    S1= random.choice(players)
    S2= random.choice(players)

    while (S1==S2):
        S1= random.choice(players)
        S2= random.choice(players)

    else:
        a=random.randint(1,100)
        if a%2==0:
            print(f"{S1} will ask question to {S2}")
        else:
            print(f"{S2} will ask question to {S1}")

number_of_players= int(input("Hey Tell me the count of total number of players playing: "))
name_of_the_players(number_of_players)
print("The player who are playing: ",players)

while True:
    ask=input('''Should we start the game? 
              if Yes (Press 'y') 
              if No (Press 'n')''')
    if ask=='y':
        game()
    else:
        print("Thankyou for Playing")
        break
    


