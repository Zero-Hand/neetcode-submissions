class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        x = []

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                product *= i

        for i in nums:
            if zero_count > 1:
                x.append(0)
            elif zero_count == 1:
                if i == 0:
                    x.append(product)
                else:
                    x.append(0)
            else:
                x.append(product // i)

        return x