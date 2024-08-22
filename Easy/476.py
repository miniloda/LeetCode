class Solution:
    def findComplement(self, num: int) -> int:
        base2_compliment = ""
        if num == 0:
            return 0
        while True:
            # automatically convert to compliment to reduce time and complexity
            if num == 1:
                base2_compliment = "0" + base2_compliment
                break
            base2_compliment = ("1" if num % 2 == 0 else '0') + base2_compliment
            num = num // 2
        return int(''.join(map(str, base2_compliment)), 2)


if __name__ == "__main__":
    print(Solution().findComplement(5))