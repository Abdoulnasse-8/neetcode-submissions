class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        ret_lst = [1] * len(nums)
       
        for i,num in enumerate(nums):
            ret_lst[i] = pre
            pre = pre * num
        post = 1
        for i in range(len(nums) - 1,-1,-1):
            ret_lst[i] = ret_lst[i] * post
            post = post * nums[i]
        return ret_lst