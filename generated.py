'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.
It shouldn't be altered here'''
import pyAgrum as gum
import numpy as np
'''Generated on : 06/21/15 14:44'''

def getValue(evs):
	res = {}
	v0 = gum.LabelizedVariable('a','a',2)
	v1 = gum.LabelizedVariable('b','b',2)
	v2 = gum.LabelizedVariable('c','c',2)
	v3 = gum.LabelizedVariable('d','d',2)
	v4 = gum.LabelizedVariable('e','e',2)
	P0sachant= gum.Potential()
	P0sachant.add(v0)
	P0sachant[:] = np.array([0.5598584694635381, 0.4401415305364619])
	P1sachant0= gum.Potential()
	P1sachant0.add(v1)
	P1sachant0.add(v0)
	P1sachant0[:] = np.array([[0.619136109438234, 0.38086389056176595], [0.5895434503127227, 0.4104565496872773]])
	P2sachant4_0= gum.Potential()
	P2sachant4_0.add(v2)
	P2sachant4_0.add(v4)
	P2sachant4_0.add(v0)
	P2sachant4_0[:] = np.array([[[0.12112807304746004, 0.8788719269525399], [0.42530664832181914, 0.5746933516781809]], [[0.41463983728906495, 0.585360162710935], [0.11954997006780317, 0.8804500299321968]]])
	P3sachant1_2= gum.Potential()
	P3sachant1_2.add(v3)
	P3sachant1_2.add(v1)
	P3sachant1_2.add(v2)
	P3sachant1_2[:] = np.array([[[0.5263819554981803, 0.4736180445018197], [0.3329920760509476, 0.6670079239490524]], [[0.4744098783414952, 0.5255901216585048], [0.622986595517999, 0.3770134044820011]]])
	P4sachant= gum.Potential()
	P4sachant.add(v4)
	P4sachant[:] = np.array([0.49707465287615615, 0.5029253471238438])
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
				Phi0_1_2_[{'c' : i2,'b' : i1,'a' : i0}] *= P0sachant[:][i0]
	for i0 in range(Phi0_1_2_.var_dims[0]):
		for i1 in range(Phi0_1_2_.var_dims[1]):
			for i2 in range(Phi0_1_2_.var_dims[2]):
				Phi0_1_2_[{'c' : i2,'b' : i1,'a' : i0}] *= P1sachant0[:][i0][i1]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'e' : i2,'c' : i1,'a' : i0}] *= P2sachant4_0[:][i2][i0][i1]
	for i0 in range(Phi1_2_3_.var_dims[0]):
		for i1 in range(Phi1_2_3_.var_dims[1]):
			for i2 in range(Phi1_2_3_.var_dims[2]):
				Phi1_2_3_[{'d' : i2,'c' : i1,'b' : i0}] *= P3sachant1_2[:][i1][i0][i2]
	for i0 in range(Phi0_2_4_.var_dims[0]):
		for i1 in range(Phi0_2_4_.var_dims[1]):
			for i2 in range(Phi0_2_4_.var_dims[2]):
				Phi0_2_4_[{'e' : i2,'c' : i1,'a' : i0}] *= P4sachant[:][i2]
	EV_1=gum.Potential()
	EV_1.add(v1)
	EV_1[:]=evs.get([1, 'b'][1])
	Phi0_1_2_.multiplicateBy(EV_1)
	EV_4=gum.Potential()
	EV_4.add(v4)
	EV_4[:]=evs.get([4, 'e'][1])
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
	res['a']=[P_0[:]]
	P_3=gum.Potential()
	P_3.add(v3)
	P_3.marginalize(Phi1_2_3_)
	P_3.normalize()
	res['d']=[P_3[:]]
	return res