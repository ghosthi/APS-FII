'''
*This part of the project wasn't coded by me.
Purpose: Use other libraries to acquire the parameters to the Damped Harmonic Oscilator.
'''

import numpy
import pandas
from matplotlib import pyplot
from scipy.optimize import curve_fit

def oha (t, a, b, o, p):
    #Função do OHA x(t) = A*e^(-b*t/[2*m])cos(o*t - p)
    return a* numpy.exp((-b*t)/(2*0.150))* numpy.cos(o*t - p)

data = pandas.read_csv('dados.csv', header = None)

t = data [0]
x = data [1]

fig, ax = pyplot.subplots(figsize = (10,7))
pyplot.plot(t, x, 'bo', ms = 2, label = 'Pontos amostrais')

pyplot.title('x(t)')
pyplot.xlabel ('t (s)')
pyplot.ylabel ('x (m)')

popt, pcov = curve_fit(oha, t, x)

pyplot.plot(t, oha(t,*popt), 'r', label = 'curve fit')

par = open('parametros_eq.txt', 'w')

w0= ((popt[1]**2)+(popt[2]**2))**0.5
q = 1/(1-(numpy.exp(-2*popt[1]*2*3.14/popt[2])))

par.write('A = ' + str(popt[0]) + '\n')
par.write('b = ' + str(popt[1]) + '\n')
par.write('W = ' + str(popt[2]) + '\n')
par.write('W0 = ' + str(w0) + '\n')
par.write('Fator de qualidade  = ' + str(q))
print('Fator de qualidade Q = ' + str(q))

pyplot.legend(loc='best')
pyplot.show()

par.close()