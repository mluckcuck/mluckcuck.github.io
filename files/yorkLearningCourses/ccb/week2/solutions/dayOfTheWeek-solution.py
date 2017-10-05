"""Checks a user input string to see if it is a weekday or a weekend day. """

weekDays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekendDays = ["saturday", "sunday"]

def checkDay(day):
        
        if day in weekDays:
                print(day, " is a weekday")
        elif day in weekendDays:
                print(day, " is a weekend day")
        else:
                print(day, " is not a day of the week")


done=False
while not done:
        day = input("Please type a day of the week or 'e' to exit: ")
        day = day.lower()
        if day == "e":
                done = True
        else:
                checkDay(day)
