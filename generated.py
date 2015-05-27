'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.
It shouldn't be altered here'''
import pyAgrum as gum
from pyAgrum import Instantiation
import numpy as numpy

'''Generated on : 05/27/15 18:28'''

def getValue(bn,evs):
	res = list()
	v0 = gum.LabelizedVariable('v0','v0',2)
	v1 = gum.LabelizedVariable('v1','v1',2)
	v2 = gum.LabelizedVariable('v2','v2',2)
	v3 = gum.LabelizedVariable('v3','v3',2)
	v4 = gum.LabelizedVariable('v4','v4',2)
	cpt0sachant=gum.Potential()
	cpt0sachant.add(v0)
	cpt0sachant[:] = numpy.array([0.0684491063186668, 0.9315508936813333])
	cpt1sachant0=gum.Potential()
	cpt1sachant0.add(v1)
	cpt1sachant0.add(v0)
	cpt1sachant0[:] = numpy.array([[0.8593976318869538, 0.14060236811304613], [0.22469567977191998, 0.77530432022808]])
	cpt2sachant40=gum.Potential()
	cpt2sachant40.add(v2)
	cpt2sachant40.add(v4)
	cpt2sachant40.add(v0)
	cpt2sachant40[:] = numpy.array([[[0.7184361675987408, 0.28156383240125915], [0.762180666627317, 0.23781933337268304]], [[0.8788476727186193, 0.12115232728138074], [0.19710247151865745, 0.8028975284813425]]])
	cpt3sachant12=gum.Potential()
	cpt3sachant12.add(v3)
	cpt3sachant12.add(v1)
	cpt3sachant12.add(v2)
	cpt3sachant12[:] = numpy.array([[[0.5146276514897381, 0.48537234851026195], [0.3306759945521494, 0.6693240054478506]], [[0.3304461566953114, 0.6695538433046886], [0.4342566418814469, 0.5657433581185531]]])
	cpt4sachant=gum.Potential()
	cpt4sachant.add(v4)
	cpt4sachant[:] = numpy.array([0.9311941616086127, 0.06880583839138729])
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
	instPot = gum.Instantiation(Phi0_1_2_)
	n=0
	while (n<instPot.domainSize()):
		Phi0_1_2_[{'v2' : instPot.val(2),'v1' : instPot.val(1),'v0' : instPot.val(0)}] *= cpt0sachant[instPot.val(0)]
		instPot.inc()
		n=n+1
	instPot = gum.Instantiation(Phi0_1_2_)
	n=0
	while (n<instPot.domainSize()):
		Phi0_1_2_[{'v2' : instPot.val(2),'v1' : instPot.val(1),'v0' : instPot.val(0)}] *= cpt1sachant0[instPot.val(0)][instPot.val(1)]
		instPot.inc()
		n=n+1
	instPot = gum.Instantiation(Phi0_2_4_)
	n=0
	while (n<instPot.domainSize()):
		Phi0_2_4_[{'v4' : instPot.val(2),'v2' : instPot.val(1),'v0' : instPot.val(0)}] *= cpt2sachant40[instPot.val(2)][instPot.val(0)][instPot.val(1)]
		instPot.inc()
		n=n+1
	instPot = gum.Instantiation(Phi1_2_3_)
	n=0
	while (n<instPot.domainSize()):
		Phi1_2_3_[{'v3' : instPot.val(2),'v2' : instPot.val(1),'v1' : instPot.val(0)}] *= cpt3sachant12[instPot.val(1)][instPot.val(0)][instPot.val(2)]
		instPot.inc()
		n=n+1
	instPot = gum.Instantiation(Phi0_2_4_)
	n=0
	while (n<instPot.domainSize()):
		Phi0_2_4_[{'v4' : instPot.val(2),'v2' : instPot.val(1),'v0' : instPot.val(0)}] *= cpt4sachant[instPot.val(2)]
		instPot.inc()
		n=n+1
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
	res.append(P_0)
	P_3=gum.Potential()
	P_3.add(v3)
	P_3.marginalize(Phi1_2_3_)
	P_3.normalize()
	res.append(P_3)
	return res