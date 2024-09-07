from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (len(rolls) + n) - sum(rolls)
        temp = sum_n // n  # note that // rounds down to the nearest integer
        if temp <= 0 or (temp >= 6 and sum_n > 6 * n):
            return []
        n_rolls = [temp] * n
        for i in range(sum_n % n):
            n_rolls[i] += 1
        return n_rolls


sol = Solution()
print(sol.missingRolls([1,2,3,4], mean=6, n=4))