"""Leet Code Programming Skills 1 study plan"""

"1523. Count Odd Numbers in an Interval Range"
"Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive)."
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # half the int's will be odd by default
        count = (high - low)//2
        # adding val of int of high or low to count because they're inclusive.
        if high%2 !=0 or low%2!= 0:
            count += 1
        
        return count

