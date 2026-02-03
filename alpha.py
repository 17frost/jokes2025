def list_jokes(**kwargs):
    list_jokes = []
    for key, value in kwargs.items():
        list_jokes.append(value)
    return list_jokes
list_jokes("robbers"==joke1, "tanks"==joke2, "pencils"==joke3)

def questions():
    ask = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if ask == joke1:
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")
        another = input("Do you want to hear another joke or are you finished? ")
    elif ask == joke2:
        input("Knock Knock ")
        input("Tank ")
        input("You are welcome! ")
        another = input("Do you want to hear another joke or are you finished? ")
    elif ask == joke3:
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
        another = input("Do you want to hear another joke or are you finished? (Type -another joke-)")
    
questions()


