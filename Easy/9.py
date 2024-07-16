class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        length = len(x_str)
        if x < 0:
            return False  # negative numbers can never be palindromes

        for i in range(0, int(length / 2)):
            if x_str[i] != x_str[length - i - 1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(0))
