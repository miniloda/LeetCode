class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        rom_to_int = 0
        i = 0
        while i < len(s):
            if i<len(s)-1 and rom_int[s[i]] < rom_int[s[i+1]]:
                rom_to_int += rom_int[s[i+1]] - rom_int[s[i]]
                i += 1
            else:
                rom_to_int += rom_int[s[i]]
            i += 1
        return rom_to_int

if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
