#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RemoveDuplicate():

    def __init__(self):
       pass

    @classmethod
    def run(cls, nums):
        nums = nums.copy()

        if len(nums) <= 0:
            return nums

        prevNum = nums[-1]
        for i,e in reversed(list(enumerate(nums))):
            if prevNum != e:
                prevNum = e;
            elif i != (len(nums)-1):
                del nums[i]
        return nums

