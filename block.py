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


class blockChain():

    def __init__(self):
        self.chain = []
        genesis = block("0000", 0, "Genesis Block")
        self.chain.append(genesis)

    def printBlockChain(self):
        for x in range(len(self.chain)):
            print(
                "Data: "+self.chain[x].data
                + "\nTime: " + self.chain[x].timeOfCreation
                + "\nHash: " + self.chain[x].blockHash
                + "\nPrevHash: " + self.chain[x].prevHash + "\n"
            )

    def getLatestHash(self):
        return self.chain[len(self.chain)-1].blockHash

    def addBlock(self, data):
        newBlock = block(blockChain.getLatestHash(self), len(self.chain), data)
        self.chain.append(newBlock)
        return


first = blockChain()
# first.printBlockChain()
#print(first.getLatestHash())
first.addBlock("Second Block")
# first.printBlockChain()
print(first)
