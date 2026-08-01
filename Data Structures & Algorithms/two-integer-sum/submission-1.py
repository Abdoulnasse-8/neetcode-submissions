class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        est_la = {}
        for i in range (len(nums)):
            rest =  target - nums[i]
            if rest in est_la:
                return [est_la[rest], i]
            est_la[nums[i]] = est_la.get(nums[i],0) + i
        return []