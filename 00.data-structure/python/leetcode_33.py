"""
search in rotated sorted array
"""
def search(nums, target):
    # find k
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            break

        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # right = mid - 1
            right = mid  # why ??

    def find(arr, t):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == t:
                return mid
            elif arr[mid] > t:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    # find target in left
    # if left == 0, then not rotated
    if left == 0:
        return find(nums, target)

    if target >= nums[0]:
        return find(nums[:left], target)
    else:
        ans = find(nums[left:], target)
        if ans != -1:
            return ans + left
        else:
            return ans


search([4,5,6,7,0,1,2], 0)
search([4,5,6,7,0,1,2], 3)
search([4,5,6,7,0,1,2], 2)
search([5,6,7,0,1,2,4], 5)
search([1], 0)
search([1], 1)
search([1, 3], 1)  # invalid test case with the condition k >= 1
