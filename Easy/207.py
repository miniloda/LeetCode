class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i,val in enumerate(nums):
            if val in hash.keys():
                return True
            else:
                hash[val] = 1
        return False