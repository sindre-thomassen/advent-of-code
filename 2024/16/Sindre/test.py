import unittest

from main import part_1, part_2, Node

class TestDay16(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.test.txt", "r") as file:
            self.MAP = [list(line.strip()) for line in file.readlines()]

        with open("input_2.test.txt", "r") as file:
            self.MAP_2 = [list(line.strip()) for line in file.readlines()]

    def test_part_1_1(self):
        res: Node = part_1(self.MAP)
        self.assertEqual(res.score, 7036)

    def test_part_1_2(self):
        res: Node = part_1(self.MAP_2)
        self.assertEqual(res.score, 11048)

    def test_part_2_1(self):
        res: Node = part_2(self.MAP)

        visited = []

        for node in res:
            visited.append(node.pos)
            while (node := node.parent) is not None:
                visited.append(node.pos)

        n_visited = len(set(visited))

        self.assertEqual(n_visited, 45)

    def test_part_2_2(self):
        res: Node = part_2(self.MAP_2)
        visited = []

        for node in res:
            visited.append(node.pos)
            while (node := node.parent) is not None:
                visited.append(node.pos)

        n_visited = len(set(visited))

        self.assertEqual(n_visited, 64)