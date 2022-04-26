import io
import sys

_INPUT = """\
6
12
345
999999999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=input()
  dp=[[0]*2 for i in range(len(N)+1)]
  for i in range(len(N)):
    dp[i+1][0]=dp[i][0]*10+dp[i][1]*int(N[i])
    if int(N[i])>1: dp[i+1][0]+=1
    if i>0:
      dp[i+1][0]+=int(N[:i]) 
    dp[i+1][1]=dp[i][1]
    if int(N[i])==1: dp[i+1][1]+=1
  print(sum(dp[-1]))