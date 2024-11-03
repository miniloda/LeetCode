class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[:i+1] == goal[-i-1:]:
                if s[i+1:] == goal[:-i-1]:
                    return True
            
        return False