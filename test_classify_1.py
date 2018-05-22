#!/usr/bin/env python3

import unittest

import classify


class TestExclude(unittest.TestCase):

	def test_marks1(self):
          results=[[1,72],[2,54],[3,51],[4,98]]
          c1 = classify.getData(results)
          self.assertEqual(c1,0)

	def test_students1(self):
	  students = [[1, AC008128], [2, AB023000], [3, AB040731], [4, AB617113]]
	  c1 = classify.thoseInRange(students, 0 , [0,3])
	  self.assertEqual(c1,4)


if __name__ == '__main__':
    unittest.main()
