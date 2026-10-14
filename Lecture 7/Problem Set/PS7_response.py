#Import relevant packages
import validators

#Capture input from users
email = input("What's your email address? ").strip()

#Pass email address into validation function
result = validators.email(email)

#Assess result and display outcome
if result == True:
    print("Valid")
else:
    print("Invalid")
