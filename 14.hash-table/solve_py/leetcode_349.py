def solve(nums1, nums2):
    """
    nums1, num2 : 정수 배열
    교집합 배열을 리턴해라
    - 각 원소는 유니크함. 순서는 상관 없음
    """
    # 둘 다 순서 정렬 -> two pointer 로 비교
    nums1.sort()
    nums2.sort()

    p1, p2 = 0, 0

    answer = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            # 교집합
            if (len(answer) == 0) or (answer[-1] != nums1[p1]):
                answer.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1


    return answer



solve([1,2,2,1], [2,2])
solve([4,9,5], [9,4,9,8,4])
