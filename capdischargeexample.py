from scipy import integrate
import math

sum1, sum2 = 0,0
r = 10
c1 = 0.05
c2 = 0.1

smallC = lambda x: math.exp(-x/(r*c1))
largeC = lambda x: math.exp(-x/(r*c2))

sum1, throwaway = integrate.quad(smallC, 0, 5)
sum2, throwaway = integrate.quad(largeC, 0, 5)

print("Small cap: %0.3fC \nLarge cap: %0.3fC" % (sum1, sum2))