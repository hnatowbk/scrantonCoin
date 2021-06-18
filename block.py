import datetime
import hashlib
import array

"""

Author: Bradley K. Hnatow

"""


class block():

    def __init__(self, prevHash, blockIndex, data):
        self.timeOfCreation = block.calculateTime()
        self.prevHash = prevHash
        self.blockIndex = blockIndex
        self.data = data
        self.blockHash = ""
        block.calculateHash(self)
        self.proofOfWork = None

# calculateTime()
# Calculates the time that the newly created block was created
# Sets the date of the block in a (Year, Day Of Week, Month, Date,
#                                  Hour, Minute, Second) format.
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


testBlock = block("jdfsjnfksndkfjs", 123, "HEY")
print()
print(testBlock.timeOfCreation)
print(testBlock.blockHash)


class blockChain():

    def __init__(self):
        self.chain = []
        genesis = block("0000", 0, "Genesis Block")
        self.chain.append(genesis)
    
    def printBlockChain(self):
        print(self.chain)

    def getLatestHash(self):
        return self.chain[len(self.chain)-1].blockHash

    def addBlock(self, data):
        newBlock = block(
            blockChain.getLatestHash(self), 
            self.chain.__len__, 
            data
        )

first = blockChain()
first.printBlockChain()
first.addBlock("FUCK")
first.printBlockChain()