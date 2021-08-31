# 6я домашка 1 задание

import unittest
import task_1


class Task1Test(unittest.TestCase):
    def test_to_dict(self):
        self.assertEqual(task_1.to_dict(('Marvel', 'DC'), ('IronMan', 'Batman')), {'Marvel': 'IronMan', 'DC': 'Batman'})

    def test2_to_dict(self):
        self.assertEqual(task_1.to_dict(('Marvel', 'DC'), ('IronMan', 'Batman')), {'Marvel': 'IronMan', 'DC': 'Joker'})

    def test3_to_dict(self):
        self.assertEqual(task_1.to_dict(('Marvel', 'DC'), ('IronMan', 'Batman')), {'Marvel': 'Hulk', 'DC': 'Batman'})

    def test4_to_dict(self):
        self.assertEqual(task_1.to_dict(('Marvel', 'DC'), ('Hulk', 'Joker')), {'Marvel': 'Hulk', 'DC': 'Joker'})


if __name__ == '__main__':
    unittest.main()
