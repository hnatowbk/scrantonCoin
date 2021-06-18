import datetime
import hashlib


class block():

    def __init__(self, prevHash, blockIndex, data):
        self.prevHash = prevHash
        self.timeOfCreation = block.calculateTime()
        self.blockIndex = blockIndex
        self.blockHash = block.calculateHash(self)
        self.data = data
        self.proofOfWork = None

    @staticmethod
    def calculateTime():
        date = datetime.datetime.now()
        setDate = date.strftime("%Y %a %b %d %H:%M:%S")
        return setDate

    def returnDate(self):
        return self.timeOfCreation

    def calculateHash(self):
        hashCode = hashlib.sha256(
            str(self.timeOfCreation).encode('utf-8')).hexdigest()
        self.blockHash = hashCode
        return

    def returnHash(self):
        return self.blockHash


testBlock = block(0, 1)
print(testBlock.returnDate())
testBlock.calculateHash()
print("")
print(testBlock.returnHash())
