name = "What is your age? "
age = int(input(name))
if age < 18:
    print("You will have just water!")
else:
    print("Mojito for you my friend!")

name = "I'm 15 years older than you. Do you know how much that is?"
age2 = int(input(name))
if age2 == age + 15:
    print("You are correct!")
else:
    print("Are you sober?")
    if input("yes/no: ") == "yes":
        print("Prove it!")
    else:
        print("Time to go home!")       