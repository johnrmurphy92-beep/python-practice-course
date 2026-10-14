#Import relevant libraries and modules
from PIL import Image
from PIL import ImageOps
import sys

#Ensure appropriate number of command-line arguments provided
if len(sys.argv) == 3: 
    pass
elif len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

#Extract paths from command line arguments and validate file type
path_input = sys.argv[1]
path_output = sys.argv[2]
if path_input.lower().endswith(".jpg") and path_output.lower().endswith(".jpg"):
    pass
elif path_input.lower().endswith(".jpeg") and path_output.lower().endswith(".jpeg"):
    pass
elif  path_input.lower().endswith(".png") and path_output.lower().endswith(".png"):
    pass
else: 
    sys.exit("Both files must use same and valid image format")

#Open the shirt image and determine its size
shirt = Image.open("shirt.png")
size = shirt.size

#Open the input image and resize it
try:
    person = Image.open(path_input)
    person_resize = ImageOps.fit(person, size)
except FileNotFoundError:
    sys.exit("File not found")

#Merge the two images and save the output
person_resize.paste(shirt, shirt)
person_resize.save(path_output)