import mpmath as mp

#a lies between 0 and pi/2 
a=float(input())
x=1/mp.cos(a)
y=1/mp.sin(a)

#computing the given equation
z=(1/(x*x))+(1/(y*y))
print(z)
