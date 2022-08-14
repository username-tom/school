# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:18:47 2020

MAGNETIC-COIL
Version: 0.0.0

   ___________
  /          /
 /__________/|
|          | |
|  ______  | |
| |     |  |_|
| |     |   _ 
| |_____|  | |
|          | |
|__________|/
@author: tomwu
"""

import math

n1_dir = -1
n2_dir = 0
n1 = 500
n2 = 200
i1 = 5
i2 = -0.5
t = 0.05
c_t = 0.08

cc_l = 0.24-0.001
lc_l = 0.24*3-0.001
rc_l = 0.24*3-0.001
lag_l = 0.001
rag_l = 0.001
meu_r = 5000
meu_0 = 4 * math.pi * 0.0000001

R_center = cc_l / (meu_0 * meu_r * t * c_t) + rag_l / (meu_0 * t * c_t)
R_left = lc_l / (meu_0 * meu_r * t * c_t)
R_right = rc_l / (meu_0 * meu_r * t * c_t)
R_ra = rag_l / (meu_0 * t * c_t)
R_la = lag_l / (meu_0 * t * c_t)

R_eq = R_center + ((R_left + R_la) * (R_right + R_ra)) / (R_left + R_right + R_ra + R_la)
flux = (n1_dir * n1 * i1 + n2_dir * n2 * i2) / R_eq
flux_r = flux * (R_right + R_ra) / (R_left + R_right + R_ra + R_la)
flux_l = flux - flux_r
fd_r = flux_r / t / c_t
fd_l = flux_l / t / c_t

"Circular core"
d_avg = 0.1
R_c = math.pi * d_avg / (meu_0 * meu_r * t * c_t)

