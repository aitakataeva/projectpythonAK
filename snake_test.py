import unittest

from snake import snake_blocks, SnakeBlock, get_randon_empty_block, COUNT_BLOCKS


class Test_test_1(unittest.TestCase):
    def test_get_random_block(self):
        global snake_blocks
        snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]

        k = get_randon_empty_block()

        self.assertTrue(k not in snake_blocks)
        self.assertTrue(k.x < COUNT_BLOCKS)
        self.assertTrue(k.y < COUNT_BLOCKS)


if __name__ == '__main__':
    unittest.main()
