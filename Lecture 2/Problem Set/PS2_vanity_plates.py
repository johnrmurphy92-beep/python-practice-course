#Define main function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Define validity check function
def is_valid(s):
    #Check length requirement      
    if len(s) > 6 or len(s) < 2:
        print("Plate must contain 2-6 characters")
        return False
    #Check restrictions on first two characters
    elif s[0:2].isalpha() == False:
        print("First two characters must be letters")
        return False  
    #Check restrictions on special characters
    elif s.isalnum() == False:
        print("Plate cannot contain spaces or punctuation")
        return False    
    #Check restrictions on number placement
    else:
        lc = 0
        nc = 0
        for l in s:
            if l.isdigit() == False:
                if nc > 0:
                    print("Letters cannot follow numbers")
                    return False
                else:
                    lc = lc + 1
            elif l.isdigit() == True:
                if nc == 0 and l == "0":
                    nc = nc + 1
                    print("First number cannot be zero")
                    return False
                else:
                    nc = nc + 1        
        return True 

#Execute main function
main()