#Request input from user
text = input("Enter text please! ")

#Replace emoji codes with emojois
text = text.replace(':)', '🙂')
text = text.replace(':(', '🙁')

#Print the resulting string
print(text)