from typing import List
from collections import defaultdict
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = defaultdict(int)
        for barcode in barcodes:
            count[barcode] = count[barcode] + 1
        # arrange the count in descending order
        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        result = [0] * len(barcodes)  # initialize the result list with all zeros
        i = 0
        for key in count:
            for _ in range(count[key]):
                result[i] = key
                i += 2
                if i >= len(barcodes):
                    i = 1
        return result
if __name__ == "__main__":
    barcodes = [1,1,1,1,2,2,3,3]
    sol = Solution()
    print(sol.rearrangeBarcodes(barcodes))