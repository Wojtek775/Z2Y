import random

possibility = ("rock","paper","scissors")
answer = ("Yes","No")


def Game():
    print("rock, paper, scissors - we play to 3 wins")
    winsA=0
    winsB=0
    while True:
        A = input("Your move - available to choose from: paper, rock, scissors: ")
        while A not in possibility:
            A = input("You can choos only from: paper, rock, scissors: ")
            
        B=str(random.choice(possibility))
        print(B)
        if A==B:
            print("draw")
        if A=="scissors" and B=="paper":
            print("you won this round")
            winsA=winsA+1
        if A=="paper" and B=="scissors":
            print("you lost this round")
            winsB=winsB+1
        if A=="rock" and B=="scissors":
            print("you won this round")
            winsA=winsA+1
        if A=="scissors" and B=="rock":
            print("you lost this round")
            winsB=winsB+1
        if A=="paper" and B=="rock":
            print("you won this round")
            winsA=winsA+1
        if A=="rock" and B=="paper":
            print("you lost this round")
            winsB=winsB+1
        if winsA==3 or winsB==3:
            break
    if winsA == 3:
        print("Congratulation You won this game!")
    else:
        print("You lost this game :(")
Game()
while True:
    replay= input("Do You want to play again? [Yes/No]]: ")
    while replay not in answer:
        replay = input("You can choos only from: Yes/No option: ")
    if replay == "Yes":
        Game()
    else:
        print("thank you for game")
        break
