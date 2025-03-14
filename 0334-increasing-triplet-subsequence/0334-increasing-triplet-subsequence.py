class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float("inf")
        second=float("inf")
        for num in nums :
            if num <=first:
                first =num
            elif num <=second:
                second= num
            else :
                return True
        return False
solution=Solution()
print(solution.increasingTriplet([1,2,3,4,5,6]))


