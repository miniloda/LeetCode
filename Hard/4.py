from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        return merged_array[len(merged_array)//2] if len(merged_array)%2 != 0 else (merged_array[len(merged_array)//2-1]+merged_array[len(merged_array)//2])/2

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1], []))