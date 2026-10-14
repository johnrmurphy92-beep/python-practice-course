#Gather input from user
email = input("What's your email? ").strip()

#Split email into username and domain
username, domain = email.split("@")

#Validate username and domain
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
