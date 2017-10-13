# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y
        num=0
        while z!=0:
            if (z&1)==1:
                num+=1
            z>>=1
        return num

if __name__ == '__main__':
    print Solution().hammingDistance(1,3)