from math import sqrt,sin,cos,tan,asin,acos,atan,atan2,degrees,radians,pi
x=(1+sqrt(5))/2
y=(x-1)/(x*x-x+1)
z=round(y-cos(radians(72)),3)
print('ans 1 = ',z)
w=round(degrees(atan(sqrt(3))),3)
print('ans 2 = ',w)
theta,phi=atan(4/3),atan(3/4)
print('ans 3 = ',round(phi,2))
print('ans 4 = ',round(round(sin(theta),4)-round(cos(phi),4),2))
print('ans 5 = ',round(sin(theta+phi)+cos(radians(w)),1))