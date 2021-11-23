class CorruptedChainError(ValueError):
    pass


class Block():
    def __init__(self):
        self.predecessor_hash = ""

    def __repr__(self):
        return f"data: {self.data}, hash: {self.hash}, predecessor hash: {self.predecessor_hash}"

    def set_data(self, data: str):
        self.data = data
        self.hash = hash(data)


class BlocksChain():
    def __init__(self):
        self.blocks = []

    def add_block(self, block: Block):
        if self.blocks:
            block.predecessor_hash = self.blocks[-1].hash
        else:
            # first block
            block.predecessor_hash = "000"
        self.blocks.append(block)

    def __repr__(self):
        blocks_repr = [block for block in self.blocks]
        return f"Blocks Chain of {len(self.blocks)} items, blocks: {blocks_repr}"

    def is_valid(self):
        for index in range(len(self.blocks)-1):
            if self.blocks[index].hash != self.blocks[index+1].predecessor_hash:
                raise CorruptedChainError("Corrupted Chain")

    def change_block(self, index: int, new_data: str):
        self.blocks[index].set_data(new_data)

    def __len__(self):
        return len(self.blocks)
