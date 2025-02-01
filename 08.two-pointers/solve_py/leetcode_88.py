"""
nums1 과 nums2 는 non-descending 순서로 정렬된 배열임 => 이 두 배열을 non-descending 순서로 병합하여 nums1 에 in-place merge
nums1 의 앞의 m 개의 원소는 실제 값이고, 뒤에 n 개의 0이 채워져 있음
m : nums1.length
n : nums2.length
0 <= m, n <= 200
1 <= m+n <= 200

O(m + n) 의 시간 복잡도 가능?
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while k > -1:
        if i < 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        elif j < 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1


    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1], 1, [], 0)
merge([3,4,5,0,0], 3, [1,1], 2)
