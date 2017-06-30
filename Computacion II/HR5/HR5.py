import math

r = int(raw_input())
p = int(raw_input())
q = int(math.pow(r,(1/float(p))))
e = [math.pow(i,p) for i in range(q+1)]
s = int(sum(e)/x)
print s
