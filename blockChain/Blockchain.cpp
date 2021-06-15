#include "Blockchain.h"

Blockchain::Blockchain() {
    _vChain.push_back(Block(0, "Genesis Block")); // Emplace_back does not
    _nDifficulty = 1;                              // work for some reason
}

void Blockchain::AddBlock(Block bNew) {
    bNew.sPrevHash = _GetLastBlock().GetHash();
    bNew.MineBlock(_nDifficulty);
    _vChain.push_back(bNew);
}

Block Blockchain::_GetLastBlock() const {
    return _vChain.back();
}

