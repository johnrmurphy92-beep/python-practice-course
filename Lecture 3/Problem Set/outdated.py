#Create a list holding months
calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#Request date from the use
while True:
    try:
        date = input("Date: ").strip()

#Process dates entered in numeric format
        if date[0].isdigit() == True:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if 0 < month <= 12 and 0 < day < 31 and 0 < year:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                pass

#Process dates entered in text format
        elif date[0].isalpha() == True and "," in date:
            month, day, year = date.split()
            month = calendar.index(month) + 1
            day = int(day.strip(','))
            year = int(year)
            if 0 < month <= 12 and 0 < day < 31 and 0 < year:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                pass

#Handle all other cases
        else:
            pass
    except ValueError: pass