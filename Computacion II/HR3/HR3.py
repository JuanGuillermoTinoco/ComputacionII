#Tercer tarea de Hacherranck
#Juan Guillermo Urincho Tinoco

g=[[i] for i in map(int,raw_input().split())]
for j in range(len(g)):
    row=map(int,raw_input().split())
    for k in range(len(g)):
        g[k].append(row[k])
for x in range(len(g)): print sum(g[x]),
