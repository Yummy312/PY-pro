from random import choice
from decouple import config


def casino_game():
    slots = [i for i in range(30)]
    MY_MONEY = config('MY_MONEY', cast=int)
    boolean = True
    while boolean:
        try:
            comp_choice = choice(slots)
            print(f"prompt: {comp_choice}")
            if MY_MONEY > 0:
                print(f"Your money: {MY_MONEY}")
                bet = int(input('Your bet:  '))
                self_choice = int(input('Your choice: '))

                if self_choice == comp_choice:
                    MY_MONEY = MY_MONEY + (bet*2)
                    print('You win ! bonus: x2')
                    question = input('Do You want continue?')

                    if question.lower() == "no":
                        print(f"You earned: {MY_MONEY}")
                        boolean = False
                else:
                    MY_MONEY = MY_MONEY - bet
                    if MY_MONEY > 0:
                        question = input('Do You want continue?')
                        if question.lower() == "no":
                            print(f"Your earned: {MY_MONEY}")
                            boolean = False
            else:
                print("You lose")
                print(f"Your money {MY_MONEY}")
                boolean = False

        except ValueError:
            print("The bet must be number")

#something





















#
# def casino_game():
#     slots = [i for i in range(30)]
#     MY_MONEY = config('MY_MONEY', cast=int)
#     boolean = True
#     before_money = MY_MONEY
#     while boolean:
#         try:
#             comp_choice = choice(slots)
#             print(f"prompt: {comp_choice}")
#             if MY_MONEY > 0:
#                 print(f"Your money: {MY_MONEY}")
#                 bet = int(input('Your bet:  '))
#                 if bet == comp_choice and MY_MONEY > 0:
#                     MY_MONEY = MY_MONEY * 2
#                     print('You win ! bonus: x2')
#                     question = input('Do You want continue?')
#                     if question.lower() == "no":
#                         print(f"You earned: {MY_MONEY}")
#                         boolean = False
#                 else:
#                     MY_MONEY = MY_MONEY - before_money
#                     if MY_MONEY > 0:
#                         question = input('Do You want continue?')
#                         print(f"Your earned: {MY_MONEY}")
#                         if question.lower() == "no":
#                             boolean = False
#             else:
#                 print("You lose")
#                 print(f"Your money {MY_MONEY}")
#                 boolean = False
#
#         except ValueError:
#             print("The bet must be number")
