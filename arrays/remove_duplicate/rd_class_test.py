#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from rd_class import RemoveDuplicate 

class testRemoveDuplicate(unittest.TestCase):

    def setUp(self):
        self.testObj = RemoveDuplicate()

    def testEmptyArray(self):
        nums = []
        result = self.testObj.run(nums)
        self.assertTrue(result == [])

    def testNoDupe(self):
        nums = [1,2,3,4]
        result = self.testObj.run(nums)
        self.assertTrue(result == nums)

    def testOneDupe(self):
        nums = [1,2,3,3,4]
        result = self.testObj.run(nums)
        self.assertTrue(result == [1,2,3,4])

    def testMultipleDupe(self):
        nums = [12,12,13,14,15,16,17,18,18]
        result = self.testObj.run(nums)
        self.assertTrue(result == [12,13,14,15,16,17,18])

    def testEndDupe(self):
        nums = [88,89,99,100,100,100,100]
        result = self.testObj.run(nums)
        self.assertTrue(result == [88,89,99,100])

    def testFrontDupe(self):
        nums = [1001,1001,1001,1001,1002,1003,1004,1004,1004,1004]
        result = self.testObj.run(nums)
        self.assertTrue(result == [1001,1002,1003,1004])

if __name__ == '__main__':
    unittest.main()
