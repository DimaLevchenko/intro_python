# 15я домашка 2е задание

import unittest
import task_4


class Task4Test(unittest.TestCase):
    def test_mobile(self):
        self.assertEqual(task_4.mobile('380699344522'), '(+38) 069 934-45-22')

    def test2_mobile(self):
        self.assertEqual(task_4.mobile('ad069934522'), 'Failed to recognize number')

    def test3_mobile(self):
        self.assertEqual(task_4.mobile('069-934-45-22'), '(+38) 069 934-45-22')


if __name__ == '__main__':
    unittest.main()
