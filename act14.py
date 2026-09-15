#age
#isemployed
#creditscore
#annualiincome
#collateral

age = int(input("Enter your age:"))
employed = bool(input("Are you currently employed?:"))
credit = int(input("Enter your credit score:"))
annual = float(input("Enter your annual income:"))
collat = bool(input("Collateral:"))

base = 0.0

if age >= 21 and employed == True:
    print("Accepted baseline criteria.")
    print("Employed?:", employed)
    if credit >=750:
        print("High credit score", credit)

        if annual >= 100000:    
            base = 4.5
            print("Income: ", annual, "Base rate:", base, )
        else:  
            base = 5.0
            print("Income: ", annual, "Base rate:", base)
        
    elif credit >= 600 and credit <750:
            print("Your credit score is less than 750")
            if collat == True:
                base = 7.0
                print("Income: ", annual, "Base rate:", base)

                print("You have a collateral.")
    
    elif credit <=600:
        print("Rejected, Credit score too low.")
    else:
        print("Invalid details.") 
elif age <= 21 and employed == False:
    print("Rejected.")
else:
    print("Invalid input")
