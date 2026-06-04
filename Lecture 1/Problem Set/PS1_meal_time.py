#Define main function
def main():
    now = input("Enter current time in hours and minutes: ")
    now_formatted = convert(now)
    if 7.0 <= now_formatted <=8.0:
        print("breakfast time")
    elif 12.0 <= now_formatted <=13.0:
        print("lunch time")
    elif 18.0 <= now_formatted <=19.0:
        print("dinner time")

#Define time converter function
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()