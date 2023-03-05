#Greeting and instructions
print(f"Greetings! Get ready for a fairytale adventure between two elves! ")
print(f"Before we begin, there are a few questions you need to answer. ")
print(f"After typing your answer, please press the Enter key. ")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":


    #Story questions

    alignment = ['lawful good', 'neutral good', 'chaotic good', 'lawful neutral', 'neutral chaotic', 'neutral', 'lawful evil', 'neutral evil', 'chaotic evil']

    #Question 1
    fireElfName = input(f"\nChoose a name for a royal female Fire Elf: \n")
    while len(fireElfName) == 0:
        fireElfName = input(f"Please enter a name: \n")

    #Question 2
    woodElfName = input(f"\nChoose a name for a common female Wood Elf: \n")
    while len(woodElfName) == 0:
        woodElfName = input(f"Please enter a name: \n")

    #Question 3
    fireElfAlignment = input(f"\nChoose an alignment for the Fire Elf:  \n\nLawful Good \nNeutral Good \nChaotic Good \nLawful Neutral \nNeutral \nChaotic Neutral \nLawful Evil \nNeutral Evil \nChaotic Evil \n\n")
    while len(fireElfAlignment) == 0:
        fireElfAlignment = input (f"Please choose an alignment: \n")
    while fireElfAlignment.lower() not in alignment :
        fireElfAlignment = input("Invalid alignment. Please choose an alignment: \n")

    #Question 4
    woodElfAlignment = input(f"\nChoose an alignment for the Wood Elf: \n\nLawful Good \nNeutral Good \nChaotic Good \nLawful Neutral \nNeutral \nChaotic Neutral \nLawful Evil \nNeutral Evil \nChaotic Evil \n\n")
    while len(woodElfAlignment) == 0:
        woodElfAlignment = input (f"Please choose an alignment: \n")
    while woodElfAlignment.lower() not in  alignment :
        woodElfAlignment = input("Invalid alignment. Please choose an alignment: \n")

            
    #Question 5
    timeOfDay = input (f"\nChoose a time of day: Day or night \n\n")
    while len(timeOfDay) == 0:
        timeOfDay = input ("Please choose a time of day: \n\n")
    while timeOfDay.lower() not in ["day" , "night" ]:
        timeOfDay = input ("Invalid time of day. Please choose day or night: \n")
    print("\n")
    
    print("-" * 50)
    print(f"\n\nLet's begin... ")
    
    #Story choices

    if timeOfDay == "day" :
        print(f"\nIt was a warm, fall day when {fireElfName} was practicing her fire spells in the woods behind the castle. ")
        print("Suddenly, she realized she was hoopelessly lost! ")
        print(f"Desperately trying to find her way out, {fireElfName} decided it may be time to use her magic. ")
    else:
        print(f"\nIt was a cool, fall night when {fireElfName} was practicing her fire spells in the woods behind the castle. ")
        print("Suddenly, she realized she was hoopelessly lost! ")
        print(f"Desperately trying to find her way out, {fireElfName} decided it may be time to use her magic. ")

    if timeOfDay == "day":
        print(f"\n{fireElfName} hesitated for a moment, for she was in an enchanted forest and was unsure what would happen if she used her magic against it. ")
        print(f"As a member of the royal fire elf family living in Autumnspire, all living beings had to bow their head to her. ")
        print(f"However, she wasn't confident she would be able to defend herself if the forest fought back. ")
        print(f"This left {fireElfName} needing to make a decision... ")
        print(f"\nDo you use your fire magic to burn the forest and clear your path back to the castle? ")
        print("(Keep in mind the alignment you chose.) ")
        print("\nYes, burn the enchanted forest. ")
        print("No, continue without harming the enchanted forest. ")
    else:
        print(f"\n{fireElfName} hesitated for a moment, for she was in an enchanted forest and was unsure what would happen if she used her magic against it. ")
        print(f"As a member of the royal fire family elf living in Autumnspire, all living beings had to bow their head to her. ")
        print(f"However, she wasn't confident she would be able to defend herself if the forest fought back. ")
        print(f"This left {fireElfName} needing to make a decision... ")
        print(f"\nDo you use your fire magic to burn the forest and clear your path back to the castle? ")
        print("(Keep in mind the alignment you chose.) ")
        print("\nYes, burn the enchanted forest. ")
        print("No, continue without harming the enchanted forest. ")


    #Decision 1
     
    burnForestChoice = input ("\nChoose wisely: \n")
    while len(burnForestChoice) == 0:
            burnForestChoice = input ("Please choose yes or no: \n")
    while burnForestChoice.lower() not in ["yes" , "no" ]:
            burnForestChoice = input ("Invalid choice. Please choose yes or no: \n")

    if burnForestChoice == "yes":
        print(f"\n{fireElfName} realized she was doubting her royalty and abilities. Self doubt was for the weak! ")
        print("She decided not to let her fear of retaliaiton from the enchanted forest get in the way.")
        print(f"With absolute confidence, {fireElfName} stretched out both hands in front of her and cast Burning Hands on the enchanted forest. ")
        print("\nIn an instant, the entire forest in front of her was set ablaze from the forest floor, all the way to the top of the tallest tree. ")
    else:
        print(f"\nAlthough {fireElfName} felt the forest should bow to her, she decided to do no harm to it. ")
        print("She was determined to find her way out of the forest with no help from anyone or anything else. ")
        print("She is, however, a member of the most royal family in the land and royalty doesn't take handouts. ")


    if burnForestChoice == "yes":
        print(f"\nSuddenly {fireElfName} was abruptly, and painfully, snatched up by the trees of the enchanted forest that lay behind her.")
        print("Her hands and feet were bound, leaving her helpless. Her only choice was to scream for help. ")
    else:
        print(f"\nAfter what felt like hours of walking in circles, {fireElfName} decided to sit and take a break. ")
        print("As soon as she sat down, she heard someone call out for help. ")
        print("Or, at least... that's what she thought she heard. ")
        print("After all, she had been wandering for hours without food or water and very easily could have been halucinating. ")
        print("\nShe decided to check it out anyway.")

    if burnForestChoice == "yes":
        print(f"\n{fireElfName} screamed as loud as she could for help but the more she screamed, the tighter and more exruciating the binds became. ")
        print(f"\nThen, out of nowhere, a wood elf came running toward the trees that had {fireElfName} bound. ")
        print("With the wave of her hand, the wood elf cast Pass Without A Trace. ")
        print("Instantly, she vanished! ")
        print(f"\nWithin a few seconds, {fireElfName} could feel the wood elf unclenching the binds from the trees. ")
        print("She must have climbed all the way up the tree without them noticing!")
        print(f"Soon after, {fireElfName} was free of the tree's grasp and was able to start climbing down. ")
        print(f"\nWhen both elves finally reached the ground, {fireElfName} realized that the other elf had been injured and was badly bleeding. ")
        print("\nHowever... she also noticed that the other elf is a wood elf. ")
    else:
        print(f"\n{fireElfName} could barely make out the shape of another elf sitting on the ground. ")
        print("She quickly but carefully made her way over to the elf. ")
        print(f"When she was finally close enough, {fireElfName} saw that the elf had been injured and was badly bleeding. ")
        print("\nHowever... she also noticed that the elf is a wood elf. ")

    print("Wood elves were not royalty and should be treated as though they matter much less than fire elves. ")

    if burnForestChoice == "yes":
        print(f"\nEven though wood elves are not royalty, {fireElfName} decided she still wanted to know the name of the elf that saved her life. ")
    else:
        print(f"\nEven though wood elves are not royalty, {fireElfName} decided she still wanted to know the name of the elf asking her for help. ")

    print(f"'What is your name?', asked {fireElfName}. ")
    print(f"'{woodElfName}', she replied. ")
    print(f"{fireElfName} had two choices; she could either help the wood elf or leave her there to suffer on her own... ")
    print(f"\nDo you use your fire magic to help {woodElfName}? ")
    print("(Keep in mind the alignment you chose.) ")
    print("\nYes. Cauterize the wound. ")
    print("No. Wood elves do not deserve help from fire elves.")
    

    #Decision 2

    helpWoodElf = input ("\nChoose wisely: \n")
    while len(helpWoodElf) == 0:
        print("Please choose yes or no: \n")
    while helpWoodElf.lower() not in ["yes" , "no" ]:
        helpWoodElf = input ("Invalid choice. Please choose yes or no: \n")

    if helpWoodElf == "yes":
        print("You muster up what little energy you have left to try and cast a spell. ")
        print("Since you had been wandering for hours, you have not had time to take a rest. All of your spell slots have been expended. ")
        print("Instead of a spell, you decide to use the cantrip, Produce Flame. ")







    keepPlaying = input("\n\nDo you want to play again? Yes or no: ")