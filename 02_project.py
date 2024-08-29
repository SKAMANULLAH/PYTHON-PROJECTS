import random
computer = random.choice([-1,0,1])
you = str(input("""
                   Enter s for snake 
                   Enter w for water 
                   Enter g for gun :- """))
you_in_form_of_number = {"s":-1,"w":0,"g":1}
reverse_of_you_in_form_of_number = {-1:"Snake",0:"Water",1:"Gun"}
print(f"You choosed :- {reverse_of_you_in_form_of_number[you_in_form_of_number[you]]}\n Computer choosed :- {reverse_of_you_in_form_of_number[computer]}")
if computer == you_in_form_of_number[you] :
    print("$ Match Draw $")
else:
    if (computer -you_in_form_of_number[you])== 1 or  (computer -you_in_form_of_number[you])== -2 :
        print("You Have Won The Match")
    else:
        print("Computer Has Won The Match")
# if computer == -1  and  you_in_form_of_number[you] ==  1 : =>(computer -you_in_form_of_number[you])= -2 *
#         print("You Have Won The Match")
#     elif computer == -1  and  you_in_form_of_number[you] == 0  : => (computer -you_in_form_of_number[you])= -1
#         print("Computer Has Won The Match")
#     elif computer == 0  and  you_in_form_of_number[you] == -1  : => (computer -you_in_form_of_number[you])=1 *
#         print("You Have Won The Match")
#     elif computer ==  0 and  you_in_form_of_number[you] == 1  : =>(computer -you_in_form_of_number[you])=-1
#         print("Computer Has Won The Match")
#     elif computer == 1  and  you_in_form_of_number[you] == -1  : => (computer -you_in_form_of_number[you])=2
#         print("Computer Has Won The Match")
#     elif computer == 1  and  you_in_form_of_number[you] == 0  : =>(computer -you_in_form_of_number[you])=1 *
#         print("You Have Won The Match")