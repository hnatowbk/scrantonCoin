import hashlib

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