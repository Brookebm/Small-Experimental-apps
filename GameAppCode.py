#put world names

world1 = "UnNamedWorld1"
world2 = "UnNamedWorld2"

#Get player name
name = input ("Please tell me your name:")

#Welcome to level/world
print ("Hi " + str(name) + "! Welcome to " + str(world1) + ". Let's begin!")
print ("Welcome back " + str(name) + "! " + str(world2) + " welcomes you!")

#Answering Questions
answer = input ("How do you write 'grey' in spanish?")
realanswer = "gris" or "Gris"
if answer == realanswer:
    print ("Correct! The answer is 'gris' regardless of if singular or plural, or gender.")
else:
    print ("Incorrect! The answer is 'gris' regardless of if singular or plural, or gender.")
