# -*- coding: utf-8 -*-
N = int(raw_input())
cnt = 0
dic = {}
 
for _ in xrange(N):

# Get reverse order of string
	rs = ''.join(sorted(raw_input()))
  
# Records the number of occurrences of a string
	if rs in dic:
		cnt += dic[rs]
		dic[rs] += 1
	else:
		dic[rs] = 1

print cnt
