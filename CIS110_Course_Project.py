#Greeting and instructions
print(f"Greetings! Get ready for a fairytale adventure between two elves! ")
print(f"Before we begin, there are a few questions you need to answer. ")
print(f"After typing your answer, please press the Enter key. ")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #Story questions
    #Question 1
    fireElfName = input(f"\nChoose a name for a royal Fire Elf: \n")
    while len(fireElfName) == 0:
        fireElfName = input(f"Please enter a name: \n")

    #Question 2
    woodElfName = input(f"\nChoose a name for a common Wood Elf: \n")
    while len(woodElfName) == 0:
        woodElfName = input(f"Please enter a name: \n")

    #Question 3
    fireElfAlignment = input(f"\nChoose an alignment for the Fire Elf:  \nLawful Good \nNeutral Good \nChaotic Good \nLawful Neutral \nNeutral \nChaotic Neutral \nLawful Evil \nNeutral Evil \nChaotic Evil \n\n")
    while len(fireElfAlignment) == 0:
        fireElfAlignment = input (f"Please choose an alignment: \n")
    while fireElfAlignment.lower() not in ["lawful good", "neutral good", "chaotic good", "lawful neutral", "neutral","chaotic neutral", "lawful evil", "lawful neutral", "chaotic evil \n" ]:
        fireElfAlignment = input("Invalid aligment. Please choose an alignment: \n")

    #Question 4
    woodElfAlignment = input(f"\nChoose an alignment for the Wood Elf: \nLawful Good \nNeutral Good \nChaotic Good \nLawful Neutral \nNeutral \nChaotic Neutral \nLawful Evil \nNeutral Evil \nChaotic Evil \n\n")
    while len(woodElfAlignment) == 0:
        woodElfAlignment = input (f"Please choose an alignment: \n")
    while woodElfAlignment.lower() not in ["lawful good", "neutral good", "chaotic good", "lawful neutral", "neutral","chaotic neutral", "lawful evil", "lawful neutral", "chaotic evil \n" ]:
        woodElfAlignment = input("Invalid aligment. Please choose an alignment: \n")

            
    #Question 5
    timeOfDay = input(f"\nChoose a time of day: Day or night \n")
    while len(timeOfDay) == 0:
        timeOfDay = input ("Please choose a time of day: \n\n")
    while timeOfDay.lower() not in ["day" , "night" ]:
        timeOfDay = input ("Invalid time of day. Please choose day or night: ")
    print("\n")
    
    print("-" * 50)
    print(f"\n\nLet's begin... ")