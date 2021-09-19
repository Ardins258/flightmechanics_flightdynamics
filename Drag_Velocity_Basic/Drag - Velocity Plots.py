# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:27:00 2021

@author: ArDC
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdfhandle = PdfPages('Drag - Velocity.pdf')

cd=0.8
rhos=1.2
A=0.1
v_array = np.linspace(0,20,21)

constant = 1/2*rhos*A*cd
drag = []

for vel in v_array:
    drag.append(vel*vel*constant)
    
    
plt.plot(v_array,drag,color='orange')   
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.legend()

pdfhandle.savefig(dpi=300)
pdfhandle.close()

