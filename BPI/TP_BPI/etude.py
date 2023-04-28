#!/usr/bin/env python3

" un programme sert a definir un type Triangle "

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        chaine=(f'Point(x={self.x},y={self.y})')
        return chaine

p1=Point(1,2)
p2=Point(0,2)
p3=Point(2,2)

print(p2)
print(f'{p2}')

class Triangle :
    def _init__(self,p1,p2,p3):
        self.Points=(p1,p2,p3)

    def __str__(self):
        chaine=(f'Triangle:\n'
                   f'Point1={self.Points[0]}\n'
                   f'Point2={self.Points[1]}\n'
                   f'Point3={self.Points[2]}\n')
        return chaine

t=Triangle()
t.Points=(p1,p2,p3)
print(t)