from __future__ import print_function
import numpy
#NumPy is a library that includes functions for matrix operations
#First line is for version compatibility

#instantiate 5x5 matrix of linear coefficients for given circuit
R = numpy.array(([1,0,3,0,0],[0,0,-3,4,5],[0,-2,0,4,0],[-1,1,1,1,0],[-1,0,1,0,1]))

#initialize value of first electromotive force
e1 = 11.501

#compute (matrix1, matrix2) inverts the first matrix, assigns it to variable m1s (Matrix1*), multiplies it by the second matrix
#and returns the resultant matrix
def computeI(m1, m2):
	m1s = numpy.linalg.inv(m1)
	return numpy.dot(m1s,m2)

while (e1 >= 11.498):
	#instantiate 5x1 matrix
	E = numpy.array(([e1],[6],[6],[0],[0]))
	I = computeI(R,E)
	i2 = round(I.item((1)), 5)
	print ('While e1 equals %s, i2 equals %s' % (e1, i2))
	e1 -= .001
