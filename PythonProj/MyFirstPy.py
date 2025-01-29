

Name = input("Patient Name: ")
B_Year = float(input("Birth Year:  "))
C_Year = 2025
Age = float(C_Year) - B_Year
print("Approx. Age: " + str(Age))
Loyalty = input("Are you a new patient? Yes or No?: ")
if Loyalty == "Yes":
    print("Welcome to our clinic, " + Name + ".")
else: 
    print("Welcome back, Friend.")
if Age > 49:
    print("You are strongly encouraged to have a colonoscopy every five years.")
elif Age > 44:
    print("If you have not yet had a colonoscopy, you are encouraged to schedule one.")




    
    
    


