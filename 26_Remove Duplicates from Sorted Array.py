def removeDuplicates(nums):
    if not nums:
        return 0  # 배열이 비어 있는 경우
    
    i = 0  # 고유 요소를 저장할 위치
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]  # 고유 요소를 저장
    
    return i + 1  # 고유 요소 개수

nums = [1, 1, 2]
removeDuplicates(nums)