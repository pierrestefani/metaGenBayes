'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.
It shouldn't be altered here'''
import pyAgrum as gum
<<<<<<< HEAD
from pyAgrum import Instantiation
import numpy as np

'''Generated on : 05/25/15 16:21'''

def getValue(bn,evs):
	res = list()
	v0 = gum.LabelizedVariable('v0','v0',2)
	cpt_v0 = [0.9486074633800493, 0.051392536619950635]
	v1 = gum.LabelizedVariable('v1','v1',2)
	cpt_v1 = [[0.9232885743569271, 0.07671142564307291], [0.004488212815328853, 0.9955117871846711]]
	v2 = gum.LabelizedVariable('v2','v2',2)
	cpt_v2 = [[[0.7670404899878064, 0.23295951001219367], [0.29402507233682523, 0.7059749276631747]], [[0.526932056564774, 0.47306794343522596], [0.3939261662199019, 0.6060738337800982]]]
	v3 = gum.LabelizedVariable('v3','v3',2)
	cpt_v3 = [[[0.5614599953655683, 0.43854000463443166], [0.8733969730950936, 0.1266030269049064]], [[0.4120854264962695, 0.5879145735037306], [0.23470081620187946, 0.7652991837981206]]]
	v4 = gum.LabelizedVariable('v4','v4',2)
	cpt_v4 = [0.3966568855715738, 0.6033431144284261]
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
				Phi0_1_2_[{'v2' : i2,'v1' : i1,'v0' : i0}] = cpt_v0[i0]
	for i0 in range(Phi0_1_2_.var_dims[0]):
		for i1 in range(Phi0_1_2_.var_dims[1]):
			for i2 in range(Phi0_1_2_.var_dims[2]):
				Phi0_1_2_[{'v2' : i2,'v1' : i1,'v0' : i0}] = cpt_v1[i0][i1]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'v4' : i2,'v2' : i1,'v0' : i0}] = cpt_v2[i2][i0][i1]
	for i0 in range(Phi1_2_3_.var_dims[0]):
		for i1 in range(Phi1_2_3_.var_dims[1]):
			for i2 in range(Phi1_2_3_.var_dims[2]):
				Phi1_2_3_[{'v3' : i2,'v2' : i1,'v1' : i0}] = cpt_v3[i1][i0][i2]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'v4' : i2,'v2' : i1,'v0' : i0}] = cpt_v4[i2]
	EV_1=gum.Potential()
	EV_1.add(v1)
=======

'''Generated on : 05/20/15 21:04'''

def getValue(bn,evs):
	res = list()
	Phi1_2_3_=gum.Potential()
	Phi1_2_3_.add(bn.variable(1))
	Phi1_2_3_.add(bn.variable(2))
	Phi1_2_3_.add(bn.variable(3))
	Phi1_2_3_.fill(1)
	Phi0_1_2_=gum.Potential()
	Phi0_1_2_.add(bn.variable(0))
	Phi0_1_2_.add(bn.variable(1))
	Phi0_1_2_.add(bn.variable(2))
	Phi0_1_2_.fill(1)
	Phi0_2_4_=gum.Potential()
	Phi0_2_4_.add(bn.variable(0))
	Phi0_2_4_.add(bn.variable(2))
	Phi0_2_4_.add(bn.variable(4))
	Phi0_2_4_.fill(1)
	Phi0_1_2_.multiplicateBy(bn.cpt(0))
	Phi0_1_2_.multiplicateBy(bn.cpt(1))
	Phi0_2_4_.multiplicateBy(bn.cpt(2))
	Phi1_2_3_.multiplicateBy(bn.cpt(3))
	Phi0_2_4_.multiplicateBy(bn.cpt(4))
	EV_1=gum.Potential()
	EV_1.add(bn.variable(1))
>>>>>>> f554d86c6daeda2d2f9d4a6468ce726a7fd74e91
	EV_1.fill(0)
	EV_1[{'b':0}]=evs.get([1, 'b'][1])[0]
	EV_1[{'b':1}]=evs.get([1, 'b'][1])[1]
	Phi0_1_2_.multiplicateBy(EV_1)
	EV_4=gum.Potential()
<<<<<<< HEAD
	EV_4.add(v4)
=======
	EV_4.add(bn.variable(4))
>>>>>>> f554d86c6daeda2d2f9d4a6468ce726a7fd74e91
	EV_4.fill(0)
	EV_4[{'e':0}]=evs.get([4, 'e'][1])[0]
	EV_4[{'e':1}]=evs.get([4, 'e'][1])[1]
	Phi0_2_4_.multiplicateBy(EV_4)
	Psi1_2_3_xx0_1_2_=gum.Potential()
<<<<<<< HEAD
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
=======
	Psi1_2_3_xx0_1_2_.add(bn.variable(1))
	Psi1_2_3_xx0_1_2_.add(bn.variable(2))
	Psi1_2_3_xx0_1_2_.marginalize(Phi1_2_3_)
	Phi0_1_2_.multiplicateBy(Psi1_2_3_xx0_1_2_)
	Psi0_2_4_xx0_1_2_=gum.Potential()
	Psi0_2_4_xx0_1_2_.add(bn.variable(0))
	Psi0_2_4_xx0_1_2_.add(bn.variable(2))
	Psi0_2_4_xx0_1_2_.marginalize(Phi0_2_4_)
	Phi0_1_2_.multiplicateBy(Psi0_2_4_xx0_1_2_)
	Psi0_1_2_xx0_2_4_dif=gum.Potential()
	Psi0_1_2_xx0_2_4_dif.add(bn.variable(0))
	Psi0_1_2_xx0_2_4_dif.add(bn.variable(2))
	Psi0_1_2_xx0_2_4_dif.marginalize(Phi0_1_2_)
	Phi0_2_4_.multiplicateBy(Psi0_1_2_xx0_2_4_dif)
	Psi0_1_2_xx1_2_3_dif=gum.Potential()
	Psi0_1_2_xx1_2_3_dif.add(bn.variable(1))
	Psi0_1_2_xx1_2_3_dif.add(bn.variable(2))
	Psi0_1_2_xx1_2_3_dif.marginalize(Phi0_1_2_)
	Phi1_2_3_.multiplicateBy(Psi0_1_2_xx1_2_3_dif)
	P_0=gum.Potential()
	P_0.add(bn.variable(0))
>>>>>>> f554d86c6daeda2d2f9d4a6468ce726a7fd74e91
	P_0.marginalize(Phi0_1_2_)
	P_0.normalize()
	res.append(P_0)
	P_3=gum.Potential()
<<<<<<< HEAD
	P_3.add(v3)
=======
	P_3.add(bn.variable(3))
>>>>>>> f554d86c6daeda2d2f9d4a6468ce726a7fd74e91
	P_3.marginalize(Phi1_2_3_)
	P_3.normalize()
	res.append(P_3)
	return res