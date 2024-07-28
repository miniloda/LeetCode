class Solution:
    def myAtoi(self, s: str) -> int:
        int_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number = []
        num_Sign = None
        ignored = " "
        signs = ["-", "+"]
        num_seen = False
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[i] in int_list:
                number.append(s[i])
                num_seen = True
                if len(number) == 1 and num_Sign is None:
                    num_Sign = "+"
            elif s[i] == ignored:
                if num_seen and num_Sign is not None:
                    break
                if num_seen == False and num_Sign is not None:
                    break
                continue
            elif s[i] not in int_list and num_seen:
                break

            elif s[i] in signs and num_Sign is None:
                num_Sign = s[i]
            else:
                return 0
        if (num_Sign is not None and len(number) == 0) or len(number) == 0:
            return 0
        num = int(str("".join(number)))
        if num_Sign is None or num_Sign == "+":
            return num if num <= 2 ** 31 - 1 else 2 ** 31 - 1
        else:
            return -1 * num if num <= 2 ** 31 else -2 ** 31


if __name__ == "__main__":
    sol = Solution()
    print("42", sol.myAtoi("42"))
    print("   -042", sol.myAtoi("   -042"))
    print("   +  041", sol.myAtoi("   + 041"))

