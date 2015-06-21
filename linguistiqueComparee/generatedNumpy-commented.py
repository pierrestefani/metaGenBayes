'''This code was generated for python (with the numpy package) use, compiled by Compiler.py and generated with numpyGenerator.py.
It shouldn't be altered here'''

import numpy as np
'''Generated on : 06/07/15 14:46'''

def getValue(evs):
    res = {}

    P0given= np.array([0.41140236926934687, 0.5885976307306532])
    P1given0= np.array([[0.7441177631461217, 0.2558822368538783], [0.7978015114947503, 0.2021984885052497]])
    P2given4_0= np.array([[[0.8184766624829497, 0.18152333751705035], [0.5248976949862224, 0.47510230501377765]], [[0.5309107573575975, 0.4690892426424025], [0.39357443900719685, 0.6064255609928032]]])
    P3given1_2= np.array([[[0.2817086822022906, 0.7182913177977094], [0.20331470401377957, 0.7966852959862204]], [[0.3362157393512485, 0.6637842606487515], [0.2184738094772016, 0.7815261905227984]]])
    P4given= np.array([0.15938180345634045, 0.8406181965436595])

    Phi1_2_3_=np.ones((2,2,2))
    Phi0_1_2_=np.ones((2,2,2))
    Phi0_2_4_=np.ones((2,2,2))

    for i0 in range(Phi0_1_2_.shape[0]):#PH ce serait plus malin de mettre la constante
        for i1 in range(Phi0_1_2_.shape[1]):#PH ce serait plus malin de mettre la constante
            for i2 in range(Phi0_1_2_.shape[2]):#PH ce serait plus malin de mettre la constante
                Phi0_1_2_[i2][i1][i0] *= P0given[i0]
                # PH : ordre des variables ?
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
    print(evs.get('b'))
    #PH 3 initialisations ?

    for i0 in range(Phi0_1_2_.shape[0]):
        for i1 in range(Phi0_1_2_.shape[1]):
            for i2 in range(Phi0_1_2_.shape[2]):
                Phi0_1_2_[i2][i1][i0] *= EV_1[i1]
    EV_4=np.zeros((2))
    EV_4= evs.get('e')
    EV_4= evs.get('e')
    #PH 3 initialisations ?
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

    ratio = P_0[0]/P_0[1] # PH ce calcul n'est pas bon : et les variables n*aire ? :)
    P_0[0] = ratio/(ratio +1)
    P_0[1] = 1/(ratio +1)
    res['a']=[P_0[:]]
    P_3=np.zeros((2))
    for i0 in range(P_3.shape[0]):
        for j0 in range(Phi1_2_3_.shape[0]):
            for j1 in range(Phi1_2_3_.shape[1]):
                P_3[i0] += Phi1_2_3_[i0][j1][j0]
    ratio = P_3[0]/P_3[1]
    P_3[0] = ratio/(ratio +1)
    P_3[1] = 1/(ratio +1)
    res['d']=[P_3[:]]
    return res


print(getValue({"e":[1,0], "b":[0.25,0.75]}))
