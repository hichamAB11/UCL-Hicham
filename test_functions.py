import unittest
from mat_to_list import mat_to_list
from reachable_nodes import reachable

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.adj_mat = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.adj_list = [[1, 3], [2], [0], [4], [3], []]

    def test_matrix_to_list(self):
        expected_list = [[1, 3], [2], [0], [4], [2], []]
        self.assertEqual(mat_to_list(self.adj_mat), expected_list)

    def test_reachable_from_0(self):
        expected = {0, 1, 2, 3, 4}
        self.assertEqual(reachable(self.adj_list, 0), expected)

    def test_reachable_from_3(self):
        expected = {3, 4}
        self.assertEqual(reachable(self.adj_list, 3), expected)

if __name__ == "__main__":
    unittest.main()
