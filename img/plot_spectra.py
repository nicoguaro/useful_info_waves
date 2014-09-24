# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:07:56 2014

@author: Nico
"""
import numpy as np
from matplotlib import pyplot as plt


omega = np.linspace(1e-6, 4, 100)
F = np.sin(np.pi*omega)/(np.pi*omega)


plt.close('all')
plt.figure()
plt.plot(omega,F**2, 'k', lw=2)
plt.fill_between(omega[0:25], 0, (F**2)[0:25], alpha=0.4)
plt.grid()
plt.xlabel(r'$\omega$', size=15)
plt.ylabel(r'$|F|^2$', size=15)
plt.show()

plt.figure()
plt.plot(omega,F**2, 'k', lw=2)
plt.fill_between(omega[0:50], 0, (F**2)[0:50], alpha=0.4)
plt.grid()
plt.xlabel(r'$\omega$', size=15)
plt.ylabel(r'$|F|^2$', size=15)
plt.show()


plt.figure()
plt.plot(omega,F**2, 'k', lw=2)
plt.fill_between(omega[0:75], 0, (F**2)[0:75], alpha=0.4)
plt.grid()
plt.xlabel(r'$\omega$', size=15)
plt.ylabel(r'$|F|^2$', size=15)
plt.show()

plt.figure()
plt.plot(omega,F**2, 'k', lw=2)
plt.fill_between(omega, 0, (F**2), alpha=0.4)
plt.grid()
plt.xlabel(r'$\omega$', size=15)
plt.ylabel(r'$|F|^2$', size=15)
plt.show()