from itertools import permutations
dp = []
input = input()
for i = 1 to n do
    dp[i] = 1
    for j = 1 to i - 1 do
        if input[j] < input[i] then
            dp[i] = dp[i] + dp[j]
j=0
"""while 1:
    for i in permutations(range(1,j+1)):
        if 
            print i
    j+=1"""