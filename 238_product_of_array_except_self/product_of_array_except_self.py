class Solution:
    def product_of_array_except_self(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        for i in range(len(nums) - 1):
            result[i + 1] = result[i] * nums[i]

        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            result[i] *= post

        return result
