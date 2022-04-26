import io
import sys

_INPUT = """\
6
1
2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import product
  N=int(input())
  tmp=['a','b','c']
  for k in product(*[list(range(3)) for _ in range(N)]):
    print(*[tmp[k[i]] for i in range(N)],sep='')