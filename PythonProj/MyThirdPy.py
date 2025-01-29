weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    print("Weight in Lbs: " + str(weight * 2.20462))
elif unit.upper() == "L":
    print("Weight in Kg: " + str(weight / 2.20462))
else: 
    print("Invalid Entry. One more attemp remaing. Please enter either K or L.")
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        print("Weight in Lbs: " + str(weight * 2.20462))
    elif unit.upper() == "L":
        print("Weight in Kg: " + str(weight / 2.20462))
    else: 
        print("Invalid Entry.") 
    



    

