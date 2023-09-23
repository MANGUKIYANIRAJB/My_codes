import random
def get_choices():
    player_choice=input(" Enter a choice('Rock','Paper','Scissor') :")
    option=["Rock","Paper","Scissor"]
    computer_choice=random.choice(option)
    choices={"Player":player_choice, "Computer":computer_choice}
    return choices

def check_win(Player,Computer):
    #print("your choice is "+ Player+ " , & computer choice is "+Computer)
    print(f"your choice is {Player} & computer choice is {Computer}")
    if Player==Computer:
        print("it is a tie!")
    elif Player=="Rock" and Computer=="Paper":
        print("Here, Computer is winner.")
    elif Player=="Paper" and Computer=="Scissor":
        print("Here, Computer is winner.")
    elif Player=="Scissor" and Computer=="Rock":
        print("Here, Computer is winner.")
    elif Player=="Rock" and Computer=="Scissor":
        print("Here, you are winner.")
    elif Player=="Scissor" and Computer=="Paper":
        print("Here, you are winner.")
    elif Player=="Paper" and Computer=="Rock":
        print("Here, you are winner.")
    else:
        print("Sorry, no one are winner.")
Choice=get_choices()
result=check_win(Choice["Player"], Choice["Computer"])
print(result)


