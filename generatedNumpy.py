'''This code was generated for python (with the numpy package) use, compiled by Compiler.py and generated with numpyGenerator.py.
It shouldn't be altered here'''

import numpy as np
'''Generated on : 05/31/15 17:22'''

def getValue(evs):
	res = list()
	P0given= np.array([0.5229678979864633, 0.47703210201353674])
	P1given0= np.array([[0.8803144156614594, 0.11968558433854064], [0.683805609977541, 0.316194390022459]])
	P2given4_0= np.array([[[0.7056949299347295, 0.2943050700652705], [0.6526339794754846, 0.3473660205245154]], [[0.5203924586379377, 0.47960754136206235], [0.7969360516847848, 0.2030639483152153]]])
	P3given1_2= np.array([[[0.34360894435777434, 0.6563910556422257], [0.42933278092691285, 0.5706672190730872]], [[0.36118848653667596, 0.6388115134633241], [0.15197773905807088, 0.8480222609419291]]])
	P4given= np.array([0.3142941016124636, 0.6857058983875365])
	Phi1_2_3_=np.ones((2,2,2))
	Phi0_1_2_=np.ones((2,2,2))
	Phi0_2_4_=np.ones((2,2,2))
	for i0 in range(Phi0_1_2_.shape[0]):
		for i1 in range(Phi0_1_2_.shape[1]):
			for i2 in range(Phi0_1_2_.shape[2]):
				Phi0_1_2_[i2][i1][i0] *= P0given[i0]
	for i0 in range(Phi0_1_2_.shape[0]):
		for i1 in range(Phi0_1_2_.shape[1]):
			for i2 in range(Phi0_1_2_.shape[2]):
				Phi0_1_2_[i2][i1][i0] *= P1given0[i0][i1]
	for i0 in range(Phi0_2_4_.shape[0]):
		for i1 in range(Phi0_2_4_.shape[1]):
			for i2 in range(Phi0_2_4_.shape[2]):
				Phi0_2_4_[i2][i1][i0] *= P2given4_0[i2][i0][i1]
	for i0 in range(Phi1_2_3_.shape[0]):
		for i1 in range(Phi1_2_3_.shape[1]):
			for i2 in range(Phi1_2_3_.shape[2]):
				Phi1_2_3_[i2][i1][i0] *= P3given1_2[i1][i0][i2]
	for i0 in range(Phi0_2_4_.shape[0]):
		for i1 in range(Phi0_2_4_.shape[1]):
			for i2 in range(Phi0_2_4_.shape[2]):
				Phi0_2_4_[i2][i1][i0] *= P4given[i2]
	EV_1=np.zeros((2))
	EV_1= evs.get('b')
	EV_1= evs.get('b')
	for i0 in range(Phi0_1_2_.shape[0]):
		for i1 in range(Phi0_1_2_.shape[1]):
			for i2 in range(Phi0_1_2_.shape[2]):
				Phi0_1_2_[i2][i1][i0] *= EV_1[i1]
	EV_4=np.zeros((2))
	EV_4= evs.get('e')
	EV_4= evs.get('e')
	for i0 in range(Phi0_2_4_.shape[0]):
		for i1 in range(Phi0_2_4_.shape[1]):
			for i2 in range(Phi0_2_4_.shape[2]):
				Phi0_2_4_[i2][i1][i0] *= EV_4[i2]
	Psi1_2_3_xx0_1_2_=np.zeros((2,2))
	for i0 in range(Psi1_2_3_xx0_1_2_.shape[0]):
		for i1 in range(Psi1_2_3_xx0_1_2_.shape[1]):
			for j0 in range(Phi1_2_3_.shape[2]):
				Psi1_2_3_xx0_1_2_[i1][i0] += Phi1_2_3_[j0][i1][i0]
	for i0 in range(Phi0_1_2_.shape[0]):
		for i1 in range(Phi0_1_2_.shape[1]):
			for i2 in range(Phi0_1_2_.shape[2]):
				Phi0_1_2_[i2][i1][i0] *= Psi1_2_3_xx0_1_2_[i2][i1]
	Psi0_2_4_xx0_1_2_=np.zeros((2,2))
	for i0 in range(Psi0_2_4_xx0_1_2_.shape[0]):
		for i1 in range(Psi0_2_4_xx0_1_2_.shape[1]):
			for j0 in range(Phi0_2_4_.shape[2]):
				Psi0_2_4_xx0_1_2_[i1][i0] += Phi0_2_4_[j0][i1][i0]
	for i0 in range(Phi0_1_2_.shape[0]):
		for i1 in range(Phi0_1_2_.shape[1]):
			for i2 in range(Phi0_1_2_.shape[2]):
				Phi0_1_2_[i2][i1][i0] *= Psi0_2_4_xx0_1_2_[i2][i0]
	Psi0_1_2_xx0_2_4_dif=np.zeros((2,2))
	for i0 in range(Psi0_1_2_xx0_2_4_dif.shape[0]):
		for i1 in range(Psi0_1_2_xx0_2_4_dif.shape[1]):
			for j0 in range(Phi0_1_2_.shape[1]):
				Psi0_1_2_xx0_2_4_dif[i1][i0] += Phi0_1_2_[i1][j0][i0]
	for i0 in range(Phi0_2_4_.shape[0]):
		for i1 in range(Phi0_2_4_.shape[1]):
			for i2 in range(Phi0_2_4_.shape[2]):
				Phi0_2_4_[i2][i1][i0] *= Psi0_1_2_xx0_2_4_dif[i1][i0]
	Psi0_1_2_xx1_2_3_dif=np.zeros((2,2))
	for i0 in range(Psi0_1_2_xx1_2_3_dif.shape[0]):
		for i1 in range(Psi0_1_2_xx1_2_3_dif.shape[1]):
			for j0 in range(Phi0_1_2_.shape[0]):
				Psi0_1_2_xx1_2_3_dif[i1][i0] += Phi0_1_2_[i1][i0][j0]
	for i0 in range(Phi1_2_3_.shape[0]):
		for i1 in range(Phi1_2_3_.shape[1]):
			for i2 in range(Phi1_2_3_.shape[2]):
				Phi1_2_3_[i2][i1][i0] *= Psi0_1_2_xx1_2_3_dif[i1][i0]
	P_0=np.zeros((2))
	for i0 in range(P_0.shape[0]):
		for j0 in range(Phi0_1_2_.shape[1]):
			for j1 in range(Phi0_1_2_.shape[2]):
				P_0[i0] += Phi0_1_2_[j1][j0][i0]
	ratio = P_0[0]/P_0[1]
	P_0[0] = ratio/(ratio +1)
	P_0[1] = 1/(ratio +1)
	res.append(P_0)
	P_3=np.zeros((2))
	for i0 in range(P_3.shape[0]):
		for j0 in range(Phi1_2_3_.shape[0]):
			for j1 in range(Phi1_2_3_.shape[1]):
				P_3[i0] += Phi1_2_3_[i0][j1][j0]
	ratio = P_3[0]/P_3[1]
	P_3[0] = ratio/(ratio +1)
	P_3[1] = 1/(ratio +1)
	res.append(P_3)
	return res