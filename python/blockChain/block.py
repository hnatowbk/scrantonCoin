import datetime
from hashlib import sha256

class block():

    def __init__ (self, prevHash, blockIndex):
        self.prevHash = prevHash
        self.timeOfCreation = calculateTime()
        self.blockIndex = blockIndex
        self.blockHash = blockHash
        self.data = data
        self.proofOfWork = proofOfWork

    def calculateTime(self):
        date = datetime.datetime.now()
        hashDate = date.strftime("%Y %a %b %d %H:%M:%S")
        return hashDate

    def returnDate(self):
        return self.dateOfCreation


#dateOfCreation = str(calculateTime())
#blockIndex = hashlib.sha256(str(dateOfCreation).encode('utf-8'))