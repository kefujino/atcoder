### Q2
# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
a, b = map(int, raw_input().split())


if((a*b)%2 == 0):
  print "Even"
else:
  print "Odd"



### Q3
# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
s = raw_input()

print s.count("1")

### Q4
# -*- coding: utf-8 -*-
# 整数の入力
N = int(raw_input())

# 空白区切りの整数を取得
li = map(int, raw_input().split())

bool1 = True
count = 0

while bool1:
  for i in xrange(0,N):
    if li[i]%2 == 1:
      bool1 = False
      break
    else:
      li[i] = li[i]/2
      
  if bool1 == False:
    break
  else:
	count += 1
	
print count

### Q5
# -*- coding: utf-8 -*-
a,b,c,x = map(int, [input() for i in range(4)])
count = 0

for i in xrange(a+1):
    for j in xrange(b+1):
        for k in xrange(c+1):
            if (500*i + 100*j + 50*k) == x:
                count += 1
print count


### Q6
# -*- coding: utf-8 -*-

N,a,b = map(int, raw_input().split())
sum1 = 0
tmp= 0

for i in xrange(1,N+1):
    tmp = 0
    for j in xrange(1,len(str(i))+1):
        tmp += int(str(i)[0-j])
    
    if (tmp >= a) and (tmp <= b):
        sum1 += i

print sum1



### Q7
# coding: utf-8
n = int(raw_input())
li = map(int, raw_input().split())
 
li.sort(reverse=True)
 
suma = 0
sumb = 0 
 
for i in xrange(n):
    if i%2 == 0:
        suma += li[i]
    else:
        sumb += li[i]

### Q8
# coding: utf-8
n = int(raw_input())
li = map(int, [raw_input() for i in xrange(n)])

li.sort(reverse=True)

count = 1

for i in xrange(n-1):
    if li[i] > li[i+1]:
        count +=1
    else:
        continue

print count


### Q9
# coding: utf-8
# 強制終了のモジュール
import sys

N, y = map(int, raw_input().split())

y /= 1000

for i in xrange(N,-1,-1):
    for j in xrange(N-i,-1,-1):
        if (10*i + 5*j + (N-i-j) == y) and (i + j + (N-i-j) == N) and ((N-i-j) >=0):
            print i,j,(N-i-j)
            sys.exit()

print -1,-1,-1

### Q10
# coding: utf-8
import sys

n = int(raw_input())

t,x,y = 0,0,0
tempt,sumxy = 0,0

for i in xrange(n):
    ti,xi,yi = map(int, raw_input().split())
    
    tempt = abs(t - ti)
    sumxy = abs(x - xi) + abs(y - yi)
    
    if (tempt%2 == sumxy%2) and (tempt >= sumxy):
        t,x,y = ti,xi,yi
    else:
        print "No"
        sys.exit()
    
print "Yes"
        
