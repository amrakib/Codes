import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
data=[]
for _ in range(m):
 a,b,c=map(int,input().split())
 data.append((c,a,b))
data.sort()

def get(x,p):
 if p[x]!=x:
  p[x]=get(p[x],p)
 return p[x]

def join(x,y,p,r):
 rx=get(x,p)
 ry=get(y,p)
 if rx==ry:
  return 0
 if r[rx]<r[ry]:
  rx,ry=ry,rx
 if r[rx]==r[ry]:
  r[rx]+=1
 p[ry]=rx
 return 1

base=0
used=[]
track=[]
p=[i for i in range(n+1)]
r=[0]*(n+1)

for i in range(m):
 w,a,b=data[i]
 if join(a,b,p,r):
  base+=w
  used.append(i)
  track.append((a,b,w))

if len(used)!=n-1:
 print(-1)
 exit()

res=1<<60

for skip in used:
 p=[i for i in range(n+1)]
 r=[0]*(n+1)
 cnt=0
 now=0
 for i in range(m):
  if i==skip:
   continue
  w,a,b=data[i]
  if join(a,b,p,r):
   now+=w
   cnt+=1
 if cnt==n-1 and now>base:
  res=min(res,now)

left=[i for i in range(m) if i not in used]

for i in left:
 p=[j for j in range(n+1)]
 r=[0]*(n+1)
 cnt=0
 now=0
 w,a,b=data[i]
 if join(a,b,p,r):
  now+=w
  cnt+=1
 for j in range(m):
  if j==i:
   continue
  w2,a2,b2=data[j]
  if join(a2,b2,p,r):
   now+=w2
   cnt+=1
 if cnt==n-1 and now>base:
  res=min(res,now)

print(res if res!=(1<<60) else -1)
