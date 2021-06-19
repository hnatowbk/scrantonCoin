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
        self.valid = True

    def printBlockChain(self):
        for x in range(len(self.chain)):
            print(
                "Data: " + self.chain[x].data
                + "\nTime: " + self.chain[x].timeOfCreation
                + "\nHash: " + self.chain[x].blockHash
                + "\nPrevHash: " + self.chain[x].prevHash + "\n"
            )

    def getLatestHash(self):
        return str(self.chain[len(self.chain)-1].blockHash)

    def addBlock(self, data):
        newBlock = block(blockChain.getLatestHash(self), len(self.chain), data)
        self.chain.append(newBlock)
        self.testChainIntegrity()

    # ---To do---
    # Loop through the array to make sure the Hash of  x-1
    # equals the prevHash of x
    def testChainIntegrity(self):
        for x in range(len(self.chain)-1):
            if self.chain[x].blockHash == self.chain[x+1].prevHash or self.chain[x].prevHash == "0000":
                self.valid = True
            elif self.chain[x].blockHash != self.chain[x+1].prevHash:
                self.valid = False
                break
        if self.valid == True:
            print("Accepted: Block Chain is Valid.\n")
        elif self.valid == False:
            print("Error: Block Chain is invalid.\n")
        else: 
            print("Error: Something went wrong.\n")
            

testBlockChain = blockChain()
testBlockChain.printBlockChain()
testBlockChain.addBlock("Second Block")
testBlockChain.printBlockChain()
testBlockChain.addBlock("Third Block")
testBlockChain.printBlockChain()
testBlockChain.addBlock("Forth Block")
testBlockChain.printBlockChain()
testBlockChain.testChainIntegrity()
