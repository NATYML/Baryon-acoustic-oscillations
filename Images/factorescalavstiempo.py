# -*- coding: utf-8 -*-

import numpy as np 
import pylab as plt
from scipy import integrate

plt.close( "all" )

delta = 10000
a = np.linspace(1e-6,2,delta)
h = 0.71
Ho = 100*h#+- 2.5 km/s/Mpc

#-----------------E. de Friedmann-------------------------------
def function( a ):
    f = (  ome_m/a+ome_rad/a**2+ome_emp*a**2+(1-ome_o) )**(-0.5)
    return f

#-----------------WMAP \Omega = 1.0000823999999999---------------
#  
ome_emp = 0.734
ome_m = 0.266
ome_rad = 8.24e-5
ome_o = ome_rad + ome_m + ome_emp

t1 = np.zeros( delta )

for i in xrange( 0, delta ):
    t1[i]=integrate.quad(function,0 ,a[i] )[0]  
 
plt.plot( t1,a,'c-',label= ' WMAP7 Universe ') 

#-----------------\Omega = 2.0(Dominado materia, Cerrado)-----------------------------------

ome_emp = 0
ome_m = 2.0
ome_rad = 0
ome_o = ome_rad + ome_m + ome_emp

t2 = np.zeros( delta )
t2i = np.zeros( delta ) 
ai = a[::-1]

for i in xrange( 0, delta ):
    t2[i]=integrate.quad(function,0 ,a[i] )[0]  
for j in xrange( 0, delta ):
    t2i[j] = 2*t2[-1]-t2[(delta-1)-j]


plt.plot( t2,a,'g-',label= ' Universe with $\Omega_m=%1.1f$'%(ome_o)) 
plt.plot( t2i,ai,'g-') 
#-----------------Einstein De Sitter Universe-----------------------------------

ome_emp = 0
ome_m = 1.
ome_rad = 0
ome_o = ome_rad + ome_m + ome_emp

t3 = np.zeros( delta )

for i in xrange( 0, delta ):
    t3[i]=integrate.quad(function,0 ,a[i] )[0]  

plt.plot( t3,a,'r-',label= ' Einstein De Sitter Universe ' ) 

#-----------------Dominado vacio \Omega = 1.-----------------------------------

a = np.linspace(1e-6,2,delta)
ome_emp = 0.7
ome_m = 0
ome_rad = 0
ome_o = ome_rad + ome_m + ome_emp

t4 = np.zeros( delta )

for i in xrange( 0, delta ):
    t4[i]=integrate.quad(function,0 ,a[i] )[0]  
 
plt.plot( t4,a,'b-',label= ' Universe with $\Omega_\Lambda=%1.2f$'%(ome_o) ) 

#---------------------------------------------------------------------------------------
# ----------         PLOTS   -----------------------------------------------------------

plt.legend(loc='lower right')
plt.hlines(1,0,7)
plt.text( 3.1,1.01, '$a_o$',fontsize=15)
plt.xlabel('$time\ [H_o^{-1}]$',fontsize=14)
plt.ylabel('$a(t)$',fontsize=16)
plt.grid()
plt.show()