import random
print("Welcome to the 5 star INdian hospi")

Admit_or_visit = input("Do you want to visit a doctor or admit the patient? 'Admit' for admit and 'Visit' for visit ... ")

if Admit_or_visit.title() == "Admit":
    Use = [1,2,3,4,5,6,7]
    in_use = random.choice(Use)
    total_beds = 10
    print(f"We have {in_use}/10 beds in occupation")
    print(f"We have {total_beds - in_use} free")
    
    Days_to_stay = [2,3,4,5,6,7,8,9,10,15,20,25,30]
    Days = random.choice(Days_to_stay)

    Decise = input("What Decise do you have??? ")
    print(f"""Okay Let me check with the doctor... \n Talks... \n Doctor :- You need to be admited for {Days} days for {Decise} \n This will cost you 50000$ \n Thanks for the money \n Bye""")

elif Admit_or_visit.title() == "Visit":
    
    Floors = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
    Floor = random.choice(Floors)
    Decise = input("What Decise do you have??? ")
    print(f"Please proseed to {Floor} floor.")
    print("Bye")