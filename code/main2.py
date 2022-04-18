import mpmath as mp

#a lies between 0 and pi/2 
a=float(input())
x=1/mp.cos(a)
y=1/mp.sin(a)

#computing the given equation
z=(1/(x*x))+(1/(y*y))
print(z)

#plotting graph
a=np.arange(0.001,1.57,0.01)
x=1/np.cos(a)
y=1/np.sin(a)
z=(1/(x*x))+(1/(y*y))
plt.grid()
plt.plot(a,z,color='green',label = 'return values of the given function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc="upper left")

plt.show()
