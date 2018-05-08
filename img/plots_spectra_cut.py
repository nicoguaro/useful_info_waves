# -*- coding: utf-8 -*-
"""
Plot the cumulative "energy" for different spectra. This is given
by the square of the spectrum.


Author: Nicolas Guarin Zapata
Last mod: March 28, 2014
"""
from matplotlib import pyplot as plt
import numpy as np

def f_ricker(t,b):
    return (1.2*t**2/b**2 - 1.)*np.exp(-6.*t**2/b**2)
    
def g_ricker(omega,b):
    return np.sqrt(np.pi)*b**3*omega**2*np.exp(-b**2*omega**2/24)/(2*6**(2.0/3.0))
    

def f_gaussian(t, m, s):
    return 2*np.exp(-(s*t)**2/2.0)*np.cos(m*t)
    
def g_gaussian(omega, m, s):
    return 1.0/s/np.sqrt(2*np.pi)*(np.exp(-(omega - m)**2/s/s**2) 
           + np.exp(-(omega + m)**2/s/s**2))
          
          
def g_square(omega, Dt):
    return np.sin(omega*Dt/2.0)/(omega*Dt/2.0)
    
    
def g_triangle(omega, Dt):
    return (np.sin(omega*Dt/2.0)/(omega*Dt/2.0))**2

####---------- Ricker wavelet ----------###
#b = 1.0
#omega_c = 2*np.sqrt(6)/b
#npts = 1000
#omega = np.linspace(0, 4*omega_c, npts)
#F2 = g_ricker(omega, b)
#F2 = F2/max(F2)
#locs = [k*omega_c for k in range(0,5)]
#labels = [r"$0$",r"$\omega_c$", r"$2\omega_c$",r"$3\omega_c$", r"$4\omega_c$"]
#frac = [0.4506, 0.9932, 0.9999, 1.0000]
#plt.close('all')
#for k in range(0,4):
#    plt.figure(figsize=(6,4))
#    plt.plot(omega, F2, 'k', lw=2)
#    plt.fill_between(omega[0:(k+1)*npts/4],F2[0:(k+1)*npts/4], 0, color='g', alpha=0.4)
#    plt.grid()
#    plt.text(omega_c, 0.5, r"$%.2f$"%frac[k], fontsize=15)
#    xl = plt.xlabel(r'$\omega$', size=15)
#    plt.ylabel(r'$\hat{f}$', size=15)
#    plt.xlim(0,4*omega_c)
#    plt.xticks(locs,labels, size=15)
#    plt.savefig('ricker_area=%i.pdf'%(k+1), bbox_inches="tight",
#                bbox_extra_artists=[xl])
#    plt.savefig('ricker_area=%i.png'%(k+1), bbound='tight',
#                bbox_extra_artists=[xl], dpi=300)
    
    
####---------- Gaussian wavelet ----------###
#omega_0 = 2.0
#omega_s = 1.0
#npts = 1000
#omega = np.linspace(0, 6, npts)
#F2 = g_gaussian(omega, omega_0, omega_s)
#F2 = F2/max(F2)
#locs = [k for k in range(0,7)]
#labels = [r"$-2\omega_\sigma$",r"$-\omega_\sigma$", r"$0$",
#          r"$\omega_\sigma$", r"$2\omega_\sigma$", r"$3\omega_\sigma$",
#          r"$4\omega_\sigma$"]
#frac = [0.50, 0.92, 0.99, 1.00]
#plt.close('all')
#for k in range(0,4):
#    plt.figure(figsize=(6,4))
#    plt.plot(omega, F2, 'k', lw=2)
#    omega2 = np.linspace(0, 2+k, npts)
#    F22 = g_gaussian(omega2, omega_0, omega_s)
#    F22 = F22/max(F22)
#    plt.fill_between(omega2,F22, 0, color='g', alpha=0.4)
#    plt.grid()
#    plt.text(2, 0.5, r"$%.2f$"%frac[k], fontsize=15)
#    xl = plt.xlabel(r'$\omega - \omega_0$', size=15)
#    plt.ylabel(r'$\hat{f}$', size=15)
#    plt.xlim(0,6)
#    plt.xticks(locs,labels, size=15)
#    plt.savefig('gaussian_area=%i.pdf'%(k+1), bbox_inches="tight",
#                bbox_extra_artists=[xl])
#    plt.savefig('gaussian_area=%i.png'%(k+1), bbox_inches='tight',
#                bbox_extra_artists=[xl], dpi=300)
    
    

####---------- Square wavelet ----------###
#Dt = 1.0
#npts = 1000
#omega = np.linspace(1e-6, 8*np.pi, npts)
#F2 = g_square(omega, Dt)
#F2 = F2/max(F2)
#locs = [2*k*np.pi for k in range(0,5)]
#labels = [r"$0$",r"$1$", r"$2$",r"$3$", r"$4$"]
#frac = [0.77, 0.90, 0.95, 0.96]
#lims = [0.5, 1, 2, 3]
#plt.close('all')
#for k in range(0,4):
#    plt.figure(figsize=(6,4))
#    plt.plot(omega, F2, 'k', lw=2)
#    omega2 = np.linspace(1e-6, 2*lims[k]*np.pi, npts)
#    F22 = g_square(omega2, Dt)
#    F22 = F22/max(F22)
#    plt.fill_between(omega2,F22, 0, color='g', alpha=0.4)
#    plt.grid()
#    plt.text(1, 0.5, r"$%.2f$"%frac[k], fontsize=15)
#    xl = plt.xlabel(r'$\omega\Delta t/\pi$', size=15)
#    plt.ylabel(r'$\hat{f}$', size=15)
#    plt.xlim(0,8)
#    plt.xticks(locs,labels, size=15)
#    plt.savefig('square_area=%i.pdf'%(k+1), bbox_inches="tight",
#                bbox_extra_artists=[xl])
#    plt.savefig('square_area=%i.png'%(k+1), bbox_inches='tight',
#                bbox_extra_artists=[xl], dpi=300)
    
    
###---------- Triangle wavelet ----------###
Dt = 1.0
npts = 1000
omega = np.linspace(1e-6, 8*np.pi, npts)
F2 = g_triangle(omega, Dt)
F2 = F2/max(F2)
locs = [2*k*np.pi for k in range(0,5)]
labels = [r"$0$",r"$1$", r"$2$",r"$3$", r"$4$"]
frac = [0.65, 0.94, 0.99, 0.99]
lims = [0.5, 1, 2, 3]
plt.close('all')
for k in range(0,4):
    plt.figure(figsize=(6,4))
    plt.plot(omega, F2, 'k', lw=2)
    omega2 = np.linspace(1e-6, 2*lims[k]*np.pi, npts)
    F22 = g_triangle(omega2, Dt)
    F22 = F22/max(F22)
    plt.fill_between(omega2,F22, 0, color='g', alpha=0.4)
    plt.grid()
    plt.text(2*np.pi, 0.5, r"$%.2f$"%frac[k], fontsize=15)
    xl = plt.xlabel(r'$\omega\Delta t/\pi$', size=15)
    plt.ylabel(r'$\hat{f}$', size=15)
    plt.xlim(0,8)
    plt.xticks(locs,labels, size=15)
    plt.savefig('triangle_area=%i.pdf'%(k+1), bbox_inches="tight",
                bbox_extra_artists=[xl])
    plt.savefig('triangle_area=%i.png'%(k+1), bbox_inches='tight',
                bbox_extra_artists=[xl], dpi=300)


plt.show()
