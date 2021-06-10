#include <ctime>


#include "Block.h"

Block::Block(uint32_t nIndexIn, const string &sDataIn) : _nIndex(nIndexIn), _sData(sDataIn){
    _nNonce = -1;
    _tTime = time(nullptr);
}

