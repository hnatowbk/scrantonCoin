import datetime
import hashlib

"""

Author: Bradley K. Hnatow

"""


class block():

    def __init__(self, prevHash, blockIndex, data):
        self.timeOfCreation = block.calculateTime()
        self.prevHash = prevHash
        self.blockIndex = blockIndex
        self.data = data
        self.blockHash = block.calculateHash(self)
        self.proofOfWork = None

# calculateTime() 
# Calculates the time that the newly created block was created
# Sets the date of the block in a (Year, Day Of Week, Month, 
#                                  Date, Hour, Minute, Second) Format
#
# @returns setDate

    @staticmethod
    def calculateTime():
        date = datetime.datetime.now()
        setDate = date.strftime("%Y %a %b %d %H:%M:%S")
        return setDate

# calculateHash(self)
# Generates a hash for the newly created block by using 
# variables like timeOfCreation, blockIndex, and the data.
# Hash is generated using sha256
#
# @returns void

    def calculateHash(self):
        hashCode = hashlib.sha256(
            (str(self.timeOfCreation) + str(self.blockIndex) + self.data).encode('utf-8')).hexdigest()
        self.blockHash = hashCode
        return

# Simple return Methods used for testing

    def returnHash(self):
        return self.blockHash

    def returnData(self):
        return self.data

    def returnDate(self):
        return self.timeOfCreation


testBlock = block("62f8d31406ce34366a8d5112fba87826c713ec2fb43419ed5ac9ccc45cd99780",
                  107, "BRADLEY BOUGHT SCRANTONCOIN")
print("")
print(testBlock.returnDate())
testBlock.calculateHash()
print("")
print(testBlock.returnHash())
print("")
print(testBlock.returnTrans())
