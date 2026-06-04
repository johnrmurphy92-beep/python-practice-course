#Request file name from user
file = input("Enter file name including extension. ")

#Remove leading or lagging whitespace
file = file.strip()

#Standardize case of user-provided input
file = file.lower()


extension = file.split(".")[-1]
print(extension)

#Display file type based on extention
match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")