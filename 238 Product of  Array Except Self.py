def productExceptSelf(nums):
    l = len(nums)
    ans = [0] * (l)
    ans[0] = 1
    for i in range(1, l):
        ans[i] = nums[i-1] * ans[i-1]

    r = 1
    for j in reversed(range(l)):
        ans[j] = ans[j] * r
        r *= nums[j]

    return ans


print(productExceptSelf([1, 2, 3, 4, 5]))