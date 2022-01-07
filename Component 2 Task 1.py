def king():
    if name.upper() == "ARTHUR":
        print("My apologies sire, You may pass.")
        exit()


def quest():

    word = 'grail'
    
    if word in holyGrail.lower():
        print("")
    else:
        print("Only those who seek the grail may walk the bridge!\n")
        exit()

def colour():

    first_Colourcharacter = favColour[:1]
    first_Namecharacter = name[:1]
    if first_Colourcharacter.lower() == first_Namecharacter.lower():
        print("You may cross the bridge!")

    else:
        print("Incorrect, now you must be thrown into the Gorge of Eternal Peril. ")

    


if __name__ == '__main__':

    print("To pass this bridge thee must answer 3 questions!")
    name = input("What is your name? ")

    king()

    holyGrail = input("What is your quest? ")
    
    quest()

    favColour = input("What is your favourite color? ")
   
    colour()
