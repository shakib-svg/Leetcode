class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
solution=Solution()
print(solution.reverseWords("the sky is blue "))