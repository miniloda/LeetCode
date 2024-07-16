class Solution:
    def isValid(self, s: str) -> bool:
        s_copy = list(s)
        if len(s) % 2 != 0:
            return False
        pair = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        i = 0
        while 0 < len(s_copy):
            #print(s_copy)
            print(i)
            if s_copy[0] in pair.values():
                return False
            if s_copy[i] in pair.values():
                closest = i-1
                value = s_copy[i]
                print(value)
                temp = True
                while temp:
                    for key in pair.keys():
                        if pair[key] == value and s_copy[closest] == key:
                            print(f"Matched {key} with {value}")
                            s_copy.pop(closest)
                            s_copy.pop(i-1)
                            temp = False
                            i = -1 # -1+1 to fix index bug
                            break
                        if closest == 0:
                            return False
                    closest -= 1
            i+=1
        return True
if __name__ == "__main__":
    s = "[)"
    sol = Solution()
    print(sol.isValid(s))
