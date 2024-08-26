import pytest
from typing import List

class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    This function finds the longest common prefix string amongst an array of strings.

    Parameters:
    strs (List[str]): A list of strings. The length of the list is between 0 and 200.
        Each string in the list has a length between 0 and 200.

    Returns:
    str: The longest common prefix string amongst the input strings.
        If there is no common prefix, an empty string is returned.
    """
    if len(strs) <= 1:
        return "".join(strs)
    min_word = min(strs)
    strs.remove(min_word)
    prefix = ""
    not_pref = False
    for n, letter in enumerate(min_word):
        for i in range(len(strs)):
            if strs[i][n] != letter:
                not_pref = True
                break
        if not_pref:
            break
        prefix = prefix + letter
    return prefix 





sol = Solution()

def test_sol1():
    assert sol.longestCommonPrefix(["race", "racecar", "racetrack"]) == "race"

def test_sol2():
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

def test_sol3():
    assert sol.longestCommonPrefix(["","b"]) == ""