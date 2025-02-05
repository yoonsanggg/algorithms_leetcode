def longestCommonPrefix(strs):
    if not strs:
        return ""

    # 공통 접두사는 문자열 배열 중 가장 짧은 문자열의 길이를 초과할 수 없음
    min_length = min(len(s) for s in strs)
    
    low, high = 0, min_length
    
    while low <= high:
        mid = (low + high) // 2
        prefix = strs[0][:mid]
        
        if all(s.startswith(prefix) for s in strs):
            low = mid + 1
        else:
            high = mid - 1
    
    return strs[0][: (low + high) // 2]

# Example usage:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(strs1))  # Output: "fl"
print(longestCommonPrefix(strs2))  # Output: ""
