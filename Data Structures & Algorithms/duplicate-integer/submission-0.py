class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = []
        for num in nums:
            if num in tab:
                return True
            tab.append(num)
        return False