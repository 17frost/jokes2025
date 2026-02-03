#Joke Database
joke_starter=("Knock Knock", "Knock Knock", "Knock Knock")
joke_2nd_line=("Calder", "Tank", "Broken pencil")
joke_punchline=("Calder police - I've been robbed!", "You are welcome! ", "Nevermind it's pointless! ")

#Defining joke type in Database
joke_db = {
    "robbers": [joke_starter[0], joke_2nd_line[0], joke_punchline[0]],
    "tanks": [joke_starter[1], joke_2nd_line[1], joke_punchline[1]],
    "pencils": [joke_starter[2], joke_2nd_line[2], joke_punchline[2]],
}
#Getting input from user asking for which joke they would like to hear in the database

def ask_joke():
    subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

    joke_lines = joke_db[subject]

    #Taking lines out of jokes and printing them with indexing from user input. Selects the joke from the Joke_2nd_line options.

    if subject not in joke_db:
        print("Sorry, I only know jokes about robbers, tanks, or pencils.")
    elif subject in joke_db:
        for i, line in enumerate(joke_lines):
            print(f"{line}")
            input()
    return

#Restarts the ask_joke prompt to continue loop through joke database
start_over = input("Do you want to hear another joke? (Y/n) ")
if start_over == "yes":
    ask_joke
elif:
print("bye!")

    





















        
# def tell_joke():
#     print(f"Do you want to hear a joke about robbers, tanks, or pencils?"
          
#     if subject not in joke_db:
#         print("Sorry, I only know jokes about robbers, tanks, or pencils!")
#         return
    
# joke_line = joke_db[subject]

# subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

# def execute_joke(subject):
#     if subject = robbers 

