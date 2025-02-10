

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
    
        # 리스트를 순회하며 해결
        for i, num in enumerate(nums):
            # 필요한 숫자(보완 수)를 계산
            complement = target - num

            # 보완 수가 이미 딕셔너리에 있는 경우 정답 반환
            if complement in num_map:
                return [num_map[complement], i]

            # 현재 숫자와 인덱스를 딕셔너리에 저장
            num_map[num] = i

        # 문제의 조건에 따라 항상 해답이 있으므로 이 부분은 실행되지 않음
        return []

nums = [3,2,4]
target = 6
sum =Solution()
print(sum.twoSum(nums,target))
