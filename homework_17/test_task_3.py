# 11я домашка второе задание

import unittest
import task_3


class Task3Test(unittest.TestCase):
    def test_temp_calc(self):
        self.assertEqual(task_3.palindrom('IFKFI'), True)

    def test2_temp_calc(self):
        self.assertEqual(task_3.palindrom('12345'), True)

    def test3_temp_calc(self):
        self.assertEqual(task_3.palindrom('19091'), False)

    def test4_temp_calc(self):
        self.assertEqual(task_3.palindrom('rfpfr'), True)


if __name__ == '__main__':
    unittest.main()
