#Joke Database for each line
joke_starter=("Knock Knock", "Knock Knock", "Knock Knock")
joke_2nd_line=("Calder", "Tank", "Broken pencil")
joke_punchline=("Calder police - I've been robbed!", "You are welcome! ", "Nevermind it's pointless! ")
new_joke_2nd_line = added_jokes = []
#tuple_line = tuple(new_joke_2nd_line)
new_punchline0 = added_punchlines = []
#tuple_punch = tuple(new_punchline0)
#Defining joke type in Database with input response
joke_db = {
    "robbers": [joke_starter[0], joke_2nd_line[0], joke_punchline[0]],
    "tanks": [joke_starter[1], joke_2nd_line[1], joke_punchline[1]],
    "pencils": [joke_starter[2], joke_2nd_line[2], joke_punchline[2]],
}

custom_joke = subject1 =(joke_starter[0], new_joke_2nd_line, new_punchline0)
#Getting input from user asking for which joke user would like to hear in the database
print(joke_db)
def ask_joke():
    subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

    if subject not in joke_db:
        accept = input("Sorry, I only know jokes about robbers, tanks, or pencils. Would u like to add one yourself? (Y/n)")
        if accept == "y":
            response = input("what would you like to call this joke?:")
            def new_joke(**name):
                new_joke = []
                for key, value in name.items():
                    new_joke.append(value)
                return new_joke
             
            print(new_joke(New=response))
            added_jokes.append(new_joke(New=response))  
            print(new_joke_2nd_line)
            if len(added_jokes) == 1:
                punchline_response = input("what would you like the punchline to be?")
                def new_punchline(**punch):
                    new_punchline = []
                    for key, value in punch.items():
                        new_punchline.append(value)
                    return new_punchline
                print(new_punchline(Punchline=punchline_response))
                added_punchlines.append(new_punchline(Punchline=punchline_response))
            print(new_punchline0)
             #Restarts the ask_joke prompt to continue loop through joke database
            def start_again():
                start_over = input("Do you want to hear another joke? (Y/n) ".lower())
                if start_over == "y":
                    ask_joke()
                    start_again()
                elif start_over == "n":
                    print("bye!")
                    exit
                    return

        elif accept == "n":
            #Restarts the ask_joke prompt to continue loop through joke database
            def start_again():
                start_over = input("Do you want to hear another joke? (Y/n) ").lower()
                if start_over == "y":
                    ask_joke()
                    start_again()
                elif start_over == "n":
                    print("bye!")
                    exit
                    return
                
    for subject1 in custom_joke:
        for i, line in enumerate(custom_joke):
            print(f"{line}")
            input()
        return
    joke_lines = joke_db[subject]
    
    # print(joke_lines)
    # Indexing joke_db and printing them in respect to user input. Selects the joke from the Joke_2nd_line options.

    print(joke_lines)
    for subject in joke_db:
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
        exit
        return
    
start_again()

    


#  def new_joke(decision):
#     print(f"what would you like to call this joke?"
          
#     if subject not in joke_db:
#         print("Sorry, I only know jokes about robbers, tanks, or pencils!")
#         return
    
# joke_line = joke_db[subject]

# subject = input("Do you want to hear a joke about robbers, tanks, or pencils? ")

# def execute_joke(subject):
#     if subject = robbers 

