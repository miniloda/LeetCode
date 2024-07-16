class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX = 2**31 - 1
        if x < 0:
            x_reversed = int(str(x)[1:][::-1])*-1
            if x_reversed < INT32_MIN:
                return 0
        else:
            x_reversed = int(str(x)[::-1])
            if x_reversed > INT32_MAX:
                return 0
        return x_reversed


if __name__ == "__main__":
    num1 = 2147483647  # This is within the range
    num2 = -2147483648  # This is within the range
    num3 = 1534236469  # This is outside the range
    num4 = 1534236469  # This is outside the range
    sol = Solution()
    print(sol.reverse(num1))
    print(sol.reverse(num2))
    print(sol.reverse(num3))
    print(sol.reverse(num4))
