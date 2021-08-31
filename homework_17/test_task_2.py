# 7я домашка 2 задание ( 3 кейса, для разных температур)

import unittest
import task_2


class Task2Test(unittest.TestCase):
    def test_temp_calc(self):
        self.assertEqual(task_2.temp_calc(36, 'C'), {'C': 36, 'F': 96.8, 'K': 309})

    def test2_temp_calc(self):
        self.assertEqual(task_2.temp_calc(67, 'F'), {'C': 20, 'F': 67, 'K': 300})

    def test3_temp_calc(self):
        self.assertEqual(task_2.temp_calc(350, 'K'), {'C': 77, 'F': 170.6, 'K': 350})


if __name__ == '__main__':
    unittest.main()
