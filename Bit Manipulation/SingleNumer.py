
import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)


if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 2, 2, 3])
