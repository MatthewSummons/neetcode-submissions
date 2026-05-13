class Solution:
    def sanitize_str(self, s: str) -> str:
        sanitised_str = ""
        for char in s.lower():
            if char.isalnum():
                sanitised_str += char
        return sanitised_str
    def isPalindrom_Rec(self, s:str) -> bool:
        if len(s) <= 1:
            return True
        if s[0].lower() == s[-1].lower():
            return self.isPalindrom_Rec(s[1:len(s)-1])
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        s = self.sanitize_str(s)
        return self.isPalindrom_Rec(s)