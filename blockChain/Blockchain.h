#include <cstdint>
#include <vector>
#include "Block.h"

class Blockchain
{
public:
    Blockchain();
    void AddBlock(Block bNew);

private:
    uint32_t _nDifficulty;
    std::vector<Block> _vChain;
    Block _GetLastBlock() const;
};

