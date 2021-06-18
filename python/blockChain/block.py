import datetime

def calculateTime():
    date = datetime.datetime.now()
    hashDate = date.strftime("%Y%m%d%M%S")
    print (hashDate)
    printDate = date.strftime("%Y %a %b %d %H:%M:%S")
    print(printDate)

calculateTime()


class block():
    def __init__ (self, prevHash, blockIndex, data):
        self.prevHash = prevHash
        self.blockIndex = blockIndex
        self.data = data