print("Hello User!")
name = input("What is your name? ")
hours = int(input("How many hours do you work in a day? "))
if hours <0:
    print("ERROR! WORK LACKS EFFORT! PLEASE DO WORK NEXT TIME!")
    exit()
elif hours >80:
    print("ERROR! WORK HOURS IS HUMANELY IMPOSSIBLE! PLEASE SEEK THE NEAREST DOCTOR!")
elif hours >40:
    print("Unerstood!")
    wage = int(input("How much is your hourly wage?"))
    ovtmult = 1.5
    full_wage = wage*ovtmult*hours
    print(full_wage)
    if full_wage == 10000> or <19999
        print("You have an average income! ")
    else:
        print("You have a low income!")
else: 
    print("Unerstood!")
    wage = int(input("How much is your hourly wage?"))
    full_wage = wage*hours
    print(full_wage)
    if full_wage == 10000> or <19999
        print("You have an average income! ")
    else:
        print("You have a low income!")
    
print(name)
print(full_wage)
