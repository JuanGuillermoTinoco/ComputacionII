class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,x,y):
        self.x=x
        self.y=y
    def reset(self):
        self.x=0
        self.y=0
    def calculate_distance(self,otherPoint):
        x=(otherPoint.x-self.x)**2
        y=(otherPoint.y-self.y)**2
        c=(x+y)**(.5)
        return c

n=int(raw_input())
both=float(n)/2
distancias=[]
for i in range(int(both)):
    x1,y1=map(int,raw_input().split())
    punto1=Point(x1,y1)
    x2,y2=map(int,raw_input().split())
    punto2=Point(x2,y2)
    distancia=punto1.calculate_distance(punto2)
    distancias.append(distancia)

for elemento in range(len(distancias)):
    print distancias[elemento]
