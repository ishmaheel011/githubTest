fName = input("Enter first name: \n")

LName = input("Enter last name: \n")

USDSum = int(input("Enter sum of money in USD: \n"))

ContrNam = input("Enter country name: \n")

print("\n")
print("Dearest " + fName +  "\nIt is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk " +LName+ ", your long lost relative from Mapsfostol. ") 
print("My father left the sum of " + str(USDSum) + "USD for us, your distant cousins. \nUnfortunately, we cannot access the money as it is in a bank in " + ContrNam +". ")
print("I desperately need your assistance to access this money. \nI will even pay you generously, 30% of the amount - " + str(round(0.3 * USDSum,1)) + "USD, ")
print("for your help.  Please get in touch with me at this email address asap. \nYours sincerely \nFrank " + LName)