import datetime
import hashlib
import array
import json

"""
Title: Python Block Chain

Author: Bradley K. Hnatow

Description: A simple block chain program devloped in python later
to be used and updated for more complex projects.

"""


class block():

    def __init__(self, prevHash, dataArray, proof, nonce=0):
        self.timeOfCreation = block.calculateTime()
        self.prevHash = prevHash
        self.dataArray = dataArray
        self.hash = block.calculateHash(self)
        self.nonce = nonce

    # calculateTime()
    #      Calculates the time that the newly created block was created
    #      Sets the date of the block in a (Year, Day Of Week, Month, Date,
    #                                       Hour, Minute, Second) format.
    # @returns String

    @staticmethod
    def calculateTime():
        date = datetime.datetime.now()
        formalDate = date.strftime("%Y %a %b %d %H:%M:%S")
        return formalDate

    # calculateHash(self)
    #       Generates a hash for the newly created block by using
    #       variables like timeOfCreation, and the prevHash.
    #       Hash is generated using sha256
    # @returns void

    def calculateHash(self):
        hashCode = hashlib.sha256(
            (str(self.timeOfCreation) + self.prevHash).encode('utf-8')).hexdigest()
        self.hash = hashCode


class blockChain():

    def __init__(self):
        self.unconfirmed = []
        self.chain = []
        genesis = block("0000", [], )  #(self, prevHash, data, proof)
        self.chain.append(genesis)
        self.valid = True

    # printBlockChain(self)
    #      Prints the current block chain providing each
    #      block's Data, Time of creation, Hash, & PrevHash
    # @reutns void

    def printBlockChain(self):
        for x in range(len(self.chain)):
            print(
                "Data: " + self.chain[x].data
                + "\nTime: " + self.chain[x].timeOfCreation
                + "\nHash: " + self.chain[x].blockHash
                + "\nPrevHash: " + self.chain[x].prevHash + "\n"
            )

    # getLatestHash(self)
    #      Provides the latest hash of blocks in the blockChain
    # @returns String
   
    @property
    def getLatestHash(self):
        return str(self.chain[len(self.chain)-1].blockHash)

    # getLatestBlock(self)
    #      Returns the most recently added block on the chain
    # @returns <block>

    @property
    def getLatestBlock(self):
        return self.chain[-1]

    
    def addNewUnconfirmed(self,data):
        self.unconfirmed.append(data)

    # addBlock(self, data)
    #      Adds a new block to the chain array
    # @reutrns void

    def addBlock(self, data, proof):
        newBlock = block(blockChain.getLatestHash(self), len(self.chain), data)
        self.chain.append(newBlock)
        self.testChainIntegrity()

    # testChainIntegrity(self)
    #      Checks the current self.chain[x].hash and compares it to 
    #      next block in the chain's prevHash
    # @returns void

    def testChainIntegrity(self):
        for x in range(len(self.chain)-1):
            if self.chain[x].blockHash == self.chain[x+1].prevHash:
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
