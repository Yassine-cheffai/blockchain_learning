import pytest

from files.blockchain import BlocksChain, Block, CorruptedChainError


def test_create_block():
    block_yassine = Block()
    block_yassine.set_data("yassine cheffai")
    assert block_yassine.data == "yassine cheffai"


def test_creation_block_chain():
    block_chain = BlocksChain()
    block_yassine = Block()
    block_yassine.set_data("yassine cheffai")
    block_chain.add_block(block_yassine)
    assert len(block_chain) == 1


def test_invalid_block_chain():
    block_chain = BlocksChain()

    block_yassine = Block()
    block_yassine.set_data("yassine cheffai")
    block_chain.add_block(block_yassine)

    block_mohammed = Block()
    block_mohammed.set_data("mohammed cheffai")
    block_chain.add_block(block_mohammed)

    block_yasmine = Block()
    block_yasmine.set_data("yasmine cheffai")
    block_chain.add_block(block_yasmine)

    with pytest.raises(CorruptedChainError):
        block_chain.change_block(1, "houria hamdi")
        block_chain.is_valid()
