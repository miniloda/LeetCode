import pytest


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters using the sliding window algorithm.

        Parameters:
        s (str): The input string.

        Returns:
        int: The length of the longest substring without repeating characters.
        """
        if len(s) <= 1:
            return len(s)
        sub = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in sub:
                sub.append(s[i])
                if len(sub) == len(s):
                    max_len = len(s)
                    break
                if i == len(s) - 1:
                    max_len = max(max_len, len(sub))
            else:
                max_len = max(max_len, len(sub))
                sub = sub[sub.index(s[i])+1:] + [s[i]]
        return max_len


sol = Solution()

@pytest.mark.timeout(1)
def test_sol1():
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3


@pytest.mark.timeout(1)
def test_sol2():
    assert sol.lengthOfLongestSubstring("bbbbbb") == 1


@pytest.mark.timeout(1)
def test_sol3():
    assert sol.lengthOfLongestSubstring("pwwkew") == 3


@pytest.mark.timeout(1)
def test_sol4():
    assert sol.lengthOfLongestSubstring("au") == 2


@pytest.mark.timeout(1)
def test_sol5():
    assert sol.lengthOfLongestSubstring("dvdf") == 3
