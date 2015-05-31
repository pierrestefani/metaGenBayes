'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.
It shouldn't be altered here'''
import pyAgrum as gum
import numpy as np
'''Generated on : 05/31/15 17:22'''

def getValue(evs):
	res = list()
	v0 = gum.LabelizedVariable('a','a',2)
	v1 = gum.LabelizedVariable('b','b',2)
	v2 = gum.LabelizedVariable('c','c',2)
	v3 = gum.LabelizedVariable('d','d',2)
	v4 = gum.LabelizedVariable('e','e',2)
	Asachant= gum.Potential()
	Asachant.add(v0)
	Asachant[:] = np.array([0.5229678979864633, 0.47703210201353674])
	BsachantA= gum.Potential()
	BsachantA.add(v1)
	BsachantA.add(v0)
	BsachantA[:] = np.array([[0.8803144156614594, 0.11968558433854064], [0.683805609977541, 0.316194390022459]])
	CsachantEA= gum.Potential()
	CsachantEA.add(v2)
	CsachantEA.add(v4)
	CsachantEA.add(v0)
	CsachantEA[:] = np.array([[[0.7056949299347295, 0.2943050700652705], [0.6526339794754846, 0.3473660205245154]], [[0.5203924586379377, 0.47960754136206235], [0.7969360516847848, 0.2030639483152153]]])
	DsachantBC= gum.Potential()
	DsachantBC.add(v3)
	DsachantBC.add(v1)
	DsachantBC.add(v2)
	DsachantBC[:] = np.array([[[0.34360894435777434, 0.6563910556422257], [0.42933278092691285, 0.5706672190730872]], [[0.36118848653667596, 0.6388115134633241], [0.15197773905807088, 0.8480222609419291]]])
	Esachant= gum.Potential()
	Esachant.add(v4)
	Esachant[:] = np.array([0.3142941016124636, 0.6857058983875365])
	Phi1_2_3_=gum.Potential()
	Phi1_2_3_.add(v1)
	Phi1_2_3_.add(v2)
	Phi1_2_3_.add(v3)
	Phi1_2_3_.fill(1)
	Phi0_1_2_=gum.Potential()
	Phi0_1_2_.add(v0)
	Phi0_1_2_.add(v1)
	Phi0_1_2_.add(v2)
	Phi0_1_2_.fill(1)
	Phi0_2_4_=gum.Potential()
	Phi0_2_4_.add(v0)
	Phi0_2_4_.add(v2)
	Phi0_2_4_.add(v4)
	Phi0_2_4_.fill(1)
	for i0 in range(Phi0_1_2_.var_dims[0]):
		for i1 in range(Phi0_1_2_.var_dims[1]):
			for i2 in range(Phi0_1_2_.var_dims[2]):
				Phi0_1_2_[{'c' : i2,'b' : i1,'a' : i0}] *= Asachant[:][i0]
	for i0 in range(Phi0_1_2_.var_dims[0]):
		for i1 in range(Phi0_1_2_.var_dims[1]):
			for i2 in range(Phi0_1_2_.var_dims[2]):
				Phi0_1_2_[{'c' : i2,'b' : i1,'a' : i0}] *= BsachantA[:][i0][i1]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'e' : i2,'c' : i1,'a' : i0}] *= CsachantEA[:][i2][i0][i1]
	for i0 in range(Phi1_2_3_.var_dims[0]):
		for i1 in range(Phi1_2_3_.var_dims[1]):
			for i2 in range(Phi1_2_3_.var_dims[2]):
				Phi1_2_3_[{'d' : i2,'c' : i1,'b' : i0}] *= DsachantBC[:][i1][i0][i2]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'e' : i2,'c' : i1,'a' : i0}] *= Esachant[:][i2]
	EV_1=gum.Potential()
	EV_1.add(v1)
	EV_1.fill(0)
	EV_1[{'b':0}]=evs.get([1, 'b'][1])[0]
	EV_1[{'b':1}]=evs.get([1, 'b'][1])[1]
	Phi0_1_2_.multiplicateBy(EV_1)
	EV_4=gum.Potential()
	EV_4.add(v4)
	EV_4.fill(0)
	EV_4[{'e':0}]=evs.get([4, 'e'][1])[0]
	EV_4[{'e':1}]=evs.get([4, 'e'][1])[1]
	Phi0_2_4_.multiplicateBy(EV_4)
	Psi1_2_3_xx0_1_2_=gum.Potential()
	Psi1_2_3_xx0_1_2_.add(v1)
	Psi1_2_3_xx0_1_2_.add(v2)
	Psi1_2_3_xx0_1_2_.marginalize(Phi1_2_3_)
	Phi0_1_2_.multiplicateBy(Psi1_2_3_xx0_1_2_)
	Psi0_2_4_xx0_1_2_=gum.Potential()
	Psi0_2_4_xx0_1_2_.add(v0)
	Psi0_2_4_xx0_1_2_.add(v2)
	Psi0_2_4_xx0_1_2_.marginalize(Phi0_2_4_)
	Phi0_1_2_.multiplicateBy(Psi0_2_4_xx0_1_2_)
	Psi0_1_2_xx0_2_4_dif=gum.Potential()
	Psi0_1_2_xx0_2_4_dif.add(v0)
	Psi0_1_2_xx0_2_4_dif.add(v2)
	Psi0_1_2_xx0_2_4_dif.marginalize(Phi0_1_2_)
	Phi0_2_4_.multiplicateBy(Psi0_1_2_xx0_2_4_dif)
	Psi0_1_2_xx1_2_3_dif=gum.Potential()
	Psi0_1_2_xx1_2_3_dif.add(v1)
	Psi0_1_2_xx1_2_3_dif.add(v2)
	Psi0_1_2_xx1_2_3_dif.marginalize(Phi0_1_2_)
	Phi1_2_3_.multiplicateBy(Psi0_1_2_xx1_2_3_dif)
	P_0=gum.Potential()
	P_0.add(v0)
	P_0.marginalize(Phi0_1_2_)
	P_0.normalize()
	res.append(P_0[:])
	P_3=gum.Potential()
	P_3.add(v3)
	P_3.marginalize(Phi1_2_3_)
	P_3.normalize()
	res.append(P_3[:])
	return res