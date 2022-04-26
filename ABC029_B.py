import io
import sys

_INPUT = """\
6
january
february
march
april
may
june
july
august
september
october
november
december
rrrrrrrrrr
srrrrrrrrr
rsr
ssr
rrs
srsrrrrrr
rssrrrrrr
sss
rrr
srr
rsrrrrrrrr
ssrrrrrrrr
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  ans=0
  for i in range(12):
    if 'r' in input():
      ans+=1
  print(ans)