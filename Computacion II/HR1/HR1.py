import sys
arr = []
p=[]
for arr_i in xrange(6):
    arr.append(map(int,raw_input().strip().split(' ')))
for r in xrange((len(arr)-2)):
    for c in xrange((len(arr[r])-2)):
        p.append(arr[r][c:c+3]+[arr[r+1][c+1]]+arr[r+2][c:c+3])
print sum(max(p,key=lambda x: sum(x)))
