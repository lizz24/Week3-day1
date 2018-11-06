#This python program is run as a module
#DOB variable that stores the year input
DOB = int(input("Enter your year of birth:"))

#calculations to work out the Age
Age = 2018 - DOB

#Anyone below 18 years is a minor
if Age <= 18:
	print("You are a Minor")
#anyone between 18 and 36 years of age is a youth
elif Age >= 18 and Age <= 36:
    print ("Your are youth")
#Above 36 is an elder  
elif Age > 36:
    print ("You are an Elder")
