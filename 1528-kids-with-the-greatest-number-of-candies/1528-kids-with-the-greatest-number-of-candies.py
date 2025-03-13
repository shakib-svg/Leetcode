class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(candy + extraCandies) >=max_candies for candy in candies]
solution =Solution()
print(solution.kidsWithCandies([2,3,5,1,3],3))


class solution:
    def kidscandy(self ,candies:List[int],extracandies:int)->List[bool]:
        max_candies=max(candies)
        return [(candy + extracandies) >=max_candies for candy in candies]
solution =solution()
print(solution.kidscandy([1,3,4,5,6,6],2))