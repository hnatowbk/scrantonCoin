import functions.calcTime, functions.calcHash
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