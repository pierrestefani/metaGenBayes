# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pyAgrum as gum
from pyAgrum import Instantiation
import gumLib.notebook as gnb

# <codecell>

bn=gum.BayesNet()
a,b,c,d,e=[bn.add(gum.LabelizedVariable(s,s,2)) for s in 'abcde']
bn.addArc(a,b)
bn.addArc(a,c)
bn.addArc(b,d)
bn.addArc(c,d)
bn.addArc(e,c)
bn.generateCPTs()
ie = gum.LazyPropagation(bn)
jt = ie.junctionTree()
gnb.showBN(bn)

# <codecell>

print(bn.variable(1))
print(bn.cpt(1))

# <codecell>

p = gum.Potential()
v0 = gum.LabelizedVariable('v0','v0',2)
cpt_v0 = bn.cpt(0).tolist()
v1 = gum.LabelizedVariable('v1','v1',2)
cpt_v1 = bn.cpt(1).tolist()
v2 = gum.LabelizedVariable('v2','v2',2)
cpt_v2 = bn.cpt(2).tolist()
v3 = gum.LabelizedVariable('v3','v3',2)
cpt_v3 = bn.cpt(3).tolist()
v4 = gum.LabelizedVariable('v4','v4',2)
cpt_v4 = bn.cpt(4).tolist()

print(cpt_v2)
print(bn.cpt(2))


# <codecell>

jt.clique(1)
n=0
Phi_1_2_3 = gum.Potential()
Phi_1_2_3.add(v1)
Phi_1_2_3.add(v2)
Phi_1_2_3.add(v3)
Phi_1_2_3.fill(1)
i = gum.Instantiation(Phi_1_2_3)

while (n<i.domainSize()):
    #MulitplicateBy cpt1
    Phi_1_2_3[{'v1': i.val(0), 'v2': i.val(1), 'v3':i.val(2)}] = Phi_1_2_3[{'v1': i.val(0), 'v2': i.val(1), 'v3':i.val(2)}]*cpt_v1[i.val(1)][i.val(0)]
    i.inc()
    n=n+1

print(Phi_1_2_3)

n=0
i.setFirst()


while (n<i.domainSize()):
    #MultiplicateBy cpt2
    Phi_1_2_3[{'v1': i.val(0), 'v2': i.val(1), 'v3':i.val(2)}] = Phi_1_2_3[{'v1': i.val(0), 'v2': i.val(1), 'v3':i.val(2)}]*cpt_v2[i.val(2)][i.val(1)][i.val(0)]
    i.inc()
    n=n+1


print(Phi_1_2_3)
print(cpt_v2)

# <codecell>

# res += "\tv"+str(i)+" = "+str(bn.cpt(i))+"\n";
#            res += "\tPv"+str(i)+" = "+str(bn.cpt(i)[:])+"\n"
#            res += "j="+str(pyAgrum.Instantiation(bn.cpt(i)))+"\n"
#            res += "j.setFirst()\n"
#            res += "proba = []\n"
#            res += "while not j.end():\n"
#            res += "\tproba.append("+str(bn.cpt(i))+".get(j))\n"
#            res += "\tj.inc()\n"
#            res += "\tproba=np.array(proba)\n"
#            res += "\tproba=proba.reshape(3,3,3)\n"
#            j=pyAgrum.Instantiation(bn.cpt(i))
#            j.setFirst()
#            prob = []
#            while not j.end():
#                prob.append(bn.cpt(i).get(j))
#                j.inc()

