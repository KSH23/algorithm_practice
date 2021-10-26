# 9251. LCS


str1 = input()
str2 = input()
len1, len2 = len(str1), len(str2)  # 각 문자열의 길이

# dp[i][j]: str1[0: i]과 str2[0: j]의 LCS 기록
# 계산의 편의를 위해 좌측과 상단에 한 줄 더 추가
dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if str2[i - 1] == str1[j - 1]:  # 두 문자열의 알파벳이 같은 경우
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 두 문자열의 알파벳이 다른 경우
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len2][len1])