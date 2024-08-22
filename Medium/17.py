from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
    Generate all possible combinations of letters that can be formed using a given set of digits.

    Parameters:
    digits (str): A string containing the digits for which combinations need to be generated.
        Each digit should be between 2 and 9, inclusive.

    Returns:
    List[str]: A list of strings representing all possible combinations of letters.
        If the input string is empty, an empty list is returned.
        """
        if len(digits) == 0:
            return []
        digits_str = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        return self.combine(digits, digits_str)
    def combine(self, digits: str, dig_str: dict) -> List[str]:
        """
    This function generates all possible combinations of letters that can be formed using a given set of digits.
    The function uses a recursive approach to build the combinations.

    Parameters:
    digits (str): A string containing the digits for which combinations need to be generated.
    dig_str (dict): A dictionary mapping digits to their corresponding letters.

    Returns:
    List[str]: A list of strings representing all possible combinations of letters.
    """
        if len(digits) == 1:
            return list(dig_str[int(digits)])
        output = []
        res = self.combine(digits[1:], dig_str)
        corr_alph_left = list(dig_str[int(digits[0])])
        corr_alph_right = list(res)
        for i in range(len(res)):
            output += [corr_alph_left[j] + corr_alph_right[i] for j in range(len(corr_alph_left))]
        return output
if __name__ == "__main__":
    print(Solution().letterCombinations("234"))
