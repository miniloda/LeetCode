from typing import List
import pytest


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, combination):
            if len(combination) == k:
                res.append(combination)
                return
            else:
                for i in range(start, n+1):
                    backtrack(i+1,combination + [i])
        res = []
        backtrack(1,[])
        return res


def test_sol():
    sol = Solution()
    assert sol.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert sol.combine(1, 1) == [[1]]
    assert sol.combine(2, 1)
