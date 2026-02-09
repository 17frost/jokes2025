#Joshua Woodward #Alexandre 


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")




joke_starter=["Knock Knock", "Knock Knock", "Knock Knock"]
joke_2nd_line=["Calder", "Tank", "Broken pencil"]
joke_punchline=["Calder police - I've been robbed!", "You are welcome! ", "Do you want to hear another joke or are you finished? "]

joke_db=[joke_starter, joke_2nd_line, joke_punchline]

subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

def joke(subject):
    if subject == robbers:
            print(f"here'a joke about, {subject}")
    elif subject == tanks:
        print(f"here'a joke about, {subject}")
    elif subject == pencils:
        print(f"here'a joke about, {subject}")
    return

print(subject)


if joke == "no":
   "Okay suit yourself"
elif joke == "yes":
    print("Great, Let's Play")
    
    # def execute_joke(subject):
        
        
            

            



if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")


        

        

def list_jokes(**kwargs):
    list_jokes = []
    for key, value in kwargs.items():
        list_jokes.append(value)
    return list_jokes
list_jokes(joke1="Calder", joke2="Tank", joke3="Pencil")

input("Do you want to hear a joke about robbers, tanks, or pencils? ")
if input() == "Calder":
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")
    another = input("Do you want to hear another joke or are you finished? ")
elif input() == "Tank":
    input("Knock Knock ")
    input("Tank ")
    input("You are welcome! ")
    another = input("Do you want to hear another joke or are you finished? ")
elif input() == "Pencil":
    input("Knock Knock ")
    input("Broken pencil ")
    input("Nevermind, it's pointless! ")
    another = input("Do you want to hear another joke or are you finished? ")

#  def new_joke(decision):
#     print(f"what would you like to call this joke?"

#     if subject not in joke_db:
#         print("Sorry, I only know jokes about robbers, tanks, or pencils!")
#         return

# joke_line = joke_db[subject]

# subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

# def execute_joke(subject):
#     if subject = robbers 