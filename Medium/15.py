from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        unique = {

        }
        for i in range(len(nums)):
            if nums[i] in unique:
                continue
            else:
                unique[nums[i]] = i
        nums = list(unique.keys())
        print(nums)
        for i in range(len(nums)):
            fixed = nums[i]
            difference_dict = {}
            for j in range(i+1, len(nums)):
                difference = 0 - (fixed + nums[j])
                if difference in difference_dict:
                    if sorted([fixed, nums[j], difference]) in res:
                        # to duplicate duplicates in result and since order of the triplets doesnt matter
                        continue
                    res.append(sorted([fixed, nums[j], difference]))
                else:
                    difference_dict[nums[j]] = j
        return res
        # time complexity: O(n^2)


if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))