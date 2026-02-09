#Joshua Woodward & Alexandre Hernandez (Finished)
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

# Dictionary to store custom jokes added by user
custom_db = {}
#Getting input from user asking for which joke user would like to hear in the database

def ask_joke(subject=None):
    # If no subject provided, ask the user
    if subject is None:
        subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

    # Check if joke exists in either database
    if subject not in joke_db and subject not in custom_db:
        accept = input("Sorry, I don't know that joke. Would you like to add one yourself? (Y/n) ")
        if accept.lower() == "y":
            # Ask for all three parts of the joke
            second_line = input("What is the second line of the joke? ")
            punchline = input("What is the punchline? ")
            
            # Add to custom_db as a new entry using append (since lists are mutable and allow dynamic additions)
            custom_db[subject] = []
            custom_db[subject].append("Knock Knock")
            custom_db[subject].append(second_line)
            custom_db[subject].append(punchline)
            print(f"Great! Added '{subject}' to the joke database!")
            
            # Ask if they want to hear another joke
            ask_again()
            return
        elif accept.lower() == "n":
            ask_again()
            return
        else:
            ask_again()
            return


    # Get joke from whichever database it's in
    if subject in joke_db:
        joke_lines = joke_db[subject]
    else:
        joke_lines = custom_db[subject]

    # Display the joke line by line
    for line in joke_lines:
        print(f"{line}")
        input()
    
    # Ask if they want another joke
    ask_again()

def ask_again():
   #function to ask if user wants another joke
    start_over = input("Do you want to hear another joke? (Y/n) ").lower()
    if start_over == "y":
        ask_joke()
    elif start_over == "n":
        print("bye!")
    # If neither y nor n, just exit
    else:
        print("Invalid input. Exiting...")
        exit()

# Start the joke program
ask_joke()