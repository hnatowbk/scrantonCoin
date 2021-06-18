import datetime

# calculateTime() 
# Calculates the time that the newly created block was created
# Sets the date of the block in a (Year, Day Of Week, Month, 
#                                  Date, Hour, Minute, Second) Format
#
# @returns setDate

def calculateTime():
    date = datetime.datetime.now()
    setDate = date.strftime("%Y %a %b %d %H:%M:%S")
    return setDate