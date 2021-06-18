import datetime
import hashlib


class block():

    def __init__(self, prevHash, blockIndex, transaction):
        self.timeOfCreation = block.calculateTime()
        self.prevHash = prevHash
        self.blockIndex = blockIndex
        self.transaction = transaction
        self.blockHash = block.calculateHash(self)
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
            (str(self.timeOfCreation) + str(self.blockIndex) + self.transaction).encode('utf-8')).hexdigest()
        self.blockHash = hashCode
        return

    def returnHash(self):
        return self.blockHash

    def returnTrans(self):
        return self.transaction


testBlock = block("62f8d31406ce34366a8d5112fba87826c713ec2fb43419ed5ac9ccc45cd99780",
                  107, "BRADLEY BOUGHT SCRANTONCOIN")
print("")
print(testBlock.returnDate())
testBlock.calculateHash()
print("")
print(testBlock.returnHash())
print("")
print(testBlock.returnTrans())
