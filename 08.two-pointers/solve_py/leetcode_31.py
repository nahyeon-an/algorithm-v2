def next_permutation(nums: list[int]):
    """
    정수 순열 배열의 사전적 순서
    1) 오른쪽에서 왼쪽으로 조회하면서 arr[i] < arr[i+1] 을 만족하는 i 찾기
    2) i+1 부터의 원소 중에서 arr[i] 보다 큰 값중 가장 작은 값의 인덱스를 j
    3) swap(i, j)
    4) i+1 부터의 배열을 오름차순 정리
    """
    # 1. pivot
    pivot = len(nums) - 2

    while pivot >= 0:
        if nums[pivot] < nums[pivot + 1]:
            break
        pivot -= 1

    if pivot == -1:
        sorted(nums)
        # return sorted(nums)

    # 2. swap_point
    j = pivot + 1
    swap_point = j
    min_value = nums[j]
    while j < len(nums):
        if (nums[pivot] < nums[j]) and (nums[j] < min_value):
            swap_point = j
            min_value = nums[j]
        j += 1

    # 3. swap
    if pivot > -1:
        tmp_val = nums[pivot]
        nums[pivot] = nums[swap_point]
        nums[swap_point] = tmp_val

    # 4. pivot + 1 부터 오름차순 정렬
    nums[pivot+1:] = sorted(nums[pivot+1:])

    print(nums)

    # return nums
