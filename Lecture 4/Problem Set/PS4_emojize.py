#Install relevant packages
import emoji

#Prompt user for input
text = input("Input: ")

#Use imported package to display results
print(emoji.emojize(text, language='alias'))
