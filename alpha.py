# def list_jokes(**kwargs):
#     list_jokes = []
#     for key, value in kwargs.items():
#         list_jokes.append(value)
#     return list_jokes
# list_jokes("robbers"==joke1, "tanks"==joke2, "pencils"==joke3)

# def questions():
#     ask = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if ask == joke1:
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         another = input("Do you want to hear another joke or are you finished? ")
#     elif ask == joke2:
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         another = input("Do you want to hear another joke or are you finished? ")
#     elif ask == joke3:
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         another = input("Do you want to hear another joke or are you finished? (Type -another joke-)")
    
# questions()

#COPY FOR TESTING
#Joke Database for each line
joke_starter=("Knock Knock", "Knock Knock", "Knock Knock")
joke_2nd_line=("Calder", "Tank", "Broken pencil")
joke_punchline=("Calder police - I've been robbed!", "You are welcome! ", "Nevermind it's pointless! ")
#Defining joke type in Database with input response
joke_db = {
    "robbers": [joke_starter[0], joke_2nd_line[0], joke_punchline[0]],
    "tanks": [joke_starter[1], joke_2nd_line[1], joke_punchline[1]],
    "pencils": [joke_starter[2], joke_2nd_line[2], joke_punchline[2]],
}
#Getting input from user asking for which joke user would like to hear in the database

def ask_joke():
    subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

    joke_lines = joke_db[subject]

    # Indexing joke_db and printing them in respect to user input. Selects the joke from the Joke_2nd_line options.

    if subject not in joke_db:
         input("Sorry, I only know jokes about robbers, tanks, or pencils. Would u like to add one yourself? (Y/n)")
    elif subject in joke_db:
        for i, line in enumerate(joke_lines):
            print(f"{line}")
            input()
    return
ask_joke()

#Restarts the ask_joke prompt to continue loop through joke database
def start_again():
    start_over = input("Do you want to hear another joke? (Y/n) ".lower())
    if start_over == "y":
        ask_joke()
        start_again()
    elif start_over == "n":
        print("bye!")
        return
    
start_again()

 
 def punchline()
 
 
 
 
 def new_joke(**name):
    input(f"what would you like to call this joke?")
    new_joke = []
        for key, value in name.items():
            new_joke.append(value)
        return new_joke

