import random

def rps(player):
    bot = random.randrange(1,4)
    if player in [1, 2, 3]:
        if(player == 1):
            print("Player selected Rock")
            if(bot == 1):
                print("Bot selected Rock")
                return "tie"
            elif(bot == 2):
                print("Bot selected Paper")
                return "lose"
            elif(bot == 3):
                print("Bot selected Scissors")
                return "win"
        elif(player == 2):
            print("Player selected Paper")
            if(bot == 1):
                print("Bot selected Rock")
                return "win"
            elif(bot == 2):
                print("Bot selected Paper")
                return "tie"
            elif(bot == 3):
                print("Bot selected Scissors")
                return "lose"
        elif(player == 3):
            print("Player selected Scissors")
            if(bot == 1):
                print("Bot selected Rock")
                return "lose"
            elif(bot == 2):
                print("Bot selected Paper")
                return "win"
            elif(bot == 3):
                print("Bot selected Scissors")
                return "tie"
    else:
        return "error"

playerscore = 0
botscore = 0

while((playerscore !=5) and (botscore != 5)):
    playerrps = int(input("Enter weapon: (1-Rock 2-Paper 3-Scissors) "))
    x = rps(playerrps)
    if(x == "error"):
        print("unknown command")
    elif(x == "win"):
        playerscore += 1
        print(f"player won! Player Score: {playerscore} Bot Score: {botscore}")
    elif(x == "lose"):
        botscore += 1
        print(f"bot won! Player Score: {playerscore} Bot Score: {botscore}")
    elif(x == "tie"):
        print(f"tie! Player Score: {playerscore} Bot Score: {botscore}")

if(playerscore == 5):
    print(f"Player Win with {playerscore} to {botscore}")
else:
    print(f"Bot Win with {botscore} to {playerscore}")