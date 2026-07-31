class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set()
        for num in nums:
            if num in tab:
                return True
            tab.add(num)
        return False