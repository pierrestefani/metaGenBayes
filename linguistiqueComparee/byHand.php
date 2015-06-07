<?php
// This code was generated for php>5.6, compiled by Compiler.py and generated with phpGenerator.py.
// It shouldn't be altered here

//Generated on : 06/07/15 14:46'''

function getValue($evs) {
  $res=[];

  $P0given= [0.41140236926934687, 0.5885976307306532];
  $P1given0= [[0.7441177631461217, 0.2558822368538783], [0.7978015114947503, 0.2021984885052497]];
  $P2given4_0= [[[0.8184766624829497, 0.18152333751705035], [0.5248976949862224, 0.47510230501377765]], [[0.5309107573575975, 0.4690892426424025], [0.39357443900719685, 0.6064255609928032]]];
  $P3given1_2= [[[0.2817086822022906, 0.7182913177977094], [0.20331470401377957, 0.7966852959862204]], [[0.3362157393512485, 0.6637842606487515], [0.2184738094772016, 0.7815261905227984]]];
  $P4given= [0.15938180345634045, 0.8406181965436595];

  $Phi1_2_3_=array_fill(0,2,array_fill(0,2,array_fill(0,2,1.0)));
  $Phi0_1_2_=array_fill(0,2,array_fill(0,2,array_fill(0,2,1.0)));
  $Phi0_2_4_=array_fill(0,2,array_fill(0,2,array_fill(0,2,1.0)));

  for($i0=0;$i0<count($Phi0_1_2_);$i0++) // PH ce serait plus malin de mettre la constante
      for($i1=0;$i1<count($Phi0_1_2_[0]);$i1++) // PH ce serait plus malin de mettre la constante
          for($i2=0;$i2<count($Phi0_1_2_[0][0]);$i2++)// PH ce serait plus malin de mettre la constante
              $Phi0_1_2_[$i2][$i1][$i0] *= $P0given[$i0];
              # PH : ordre des variables ?
  for($i0=0;$i0<count($Phi0_1_2_);$i0++)
      for($i1=0;$i1<count($Phi0_1_2_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_1_2_[0][0]);$i2++)
              $Phi0_1_2_[$i2][$i1][$i0] *= $P1given0[$i0][$i1];
  for($i0=0;$i0<count($Phi0_2_4_);$i0++)
      for($i1=0;$i1<count($Phi0_2_4_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_2_4_[0][0]);$i2++)
              $Phi0_2_4_[$i2][$i1][$i0] *= $P2given4_0[$i2][$i0][$i1];
  for($i0=0;$i0<count($Phi1_2_3_);$i0++)
      for($i1=0;$i1<count($Phi1_2_3_[0]);$i1++)
          for($i2=0;$i2<count($Phi1_2_3_[0][0]);$i2++)
              $Phi1_2_3_[$i2][$i1][$i0] *= $P3given1_2[$i1][$i0][$i2];
  for($i0=0;$i0<count($Phi0_2_4_);$i0++)
      for($i1=0;$i1<count($Phi0_2_4_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_2_4_[0][0]);$i2++)
              $Phi0_2_4_[$i2][$i1][$i0] *= $P4given[$i2];
  $EV_1=$evs['b'];
  //EV_1= evs.get('b')
  //EV_1= evs.get('b')
  //PH 3 initialisations ?

  for($i0=0;$i0<count($Phi0_1_2_);$i0++)
      for($i1=0;$i1<count($Phi0_1_2_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_1_2_[0][0]);$i2++)
              $Phi0_1_2_[$i2][$i1][$i0] *= $EV_1[$i1];
  $EV_4=$evs['e'];
  //EV_4= evs.get('e')
  //EV_4= evs.get('e')
  //PH 3 initialisations ?
  for($i0=0;$i0<count($Phi0_2_4_);$i0++)
      for($i1=0;$i1<count($Phi0_2_4_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_2_4_[0][0]);$i2++)
              $Phi0_2_4_[$i2][$i1][$i0] *= $EV_4[$i2];
  $Psi1_2_3_xx0_1_2_=array_fill(0,2,array_fill(0,2,0.0));
  for($i0=0;$i0<count($Psi1_2_3_xx0_1_2_);$i0++)
      for($i1=0;$i1<count($Psi1_2_3_xx0_1_2_[0]);$i1++)
          for($j0=0;$j0<count($Phi1_2_3_[0][0]);$j0++)
              $Psi1_2_3_xx0_1_2_[$i1][$i0] += $Phi1_2_3_[$j0][$i1][$i0];
  for($i0=0;$i0<count($Phi0_1_2_);$i0++)
      for($i1=0;$i1<count($Phi0_1_2_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_1_2_[0][0]);$i2++)
              $Phi0_1_2_[$i2][$i1][$i0] *= $Psi1_2_3_xx0_1_2_[$i2][$i1];
  $Psi0_2_4_xx0_1_2_=array_fill(0,2,array_fill(0,2,0.0));
  for($i0=0;$i0<count($Psi0_2_4_xx0_1_2_);$i0++)
      for($i1=0;$i1<count($Psi0_2_4_xx0_1_2_[0]);$i1++)
          for($j0=0;$j0<count($Phi0_2_4_[0][0]);$j0++)
              $Psi0_2_4_xx0_1_2_[$i1][$i0] += $Phi0_2_4_[$j0][$i1][$i0];
  for($i0=0;$i0<count($Phi0_1_2_);$i0++)
      for($i1=0;$i1<count($Phi0_1_2_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_1_2_[0][0]);$i2++)
              $Phi0_1_2_[$i2][$i1][$i0] *= $Psi0_2_4_xx0_1_2_[$i2][$i0];
  $Psi0_1_2_xx0_2_4_dif=array_fill(0,2,array_fill(0,2,0.0));
  for($i0=0;$i0<count($Psi0_1_2_xx0_2_4_dif);$i0++)
      for($i1=0;$i1<count($Psi0_1_2_xx0_2_4_dif[0]);$i1++)
          for($j0=0;$j0<count($Phi0_1_2_[0]);$j0++)
              $Psi0_1_2_xx0_2_4_dif[$i1][$i0] += $Phi0_1_2_[$i1][$j0][$i0];
  for($i0=0;$i0<count($Phi0_2_4_);$i0++)
      for($i1=0;$i1<count($Phi0_2_4_[0]);$i1++)
          for($i2=0;$i2<count($Phi0_2_4_[0][0]);$i2++)
              $Phi0_2_4_[$i2][$i1][$i0] *= $Psi0_1_2_xx0_2_4_dif[$i1][$i0];
  $Psi0_1_2_xx1_2_3_dif=array_fill(0,2,array_fill(0,2,0.0));
  for($i0=0;$i0<count($Psi0_1_2_xx1_2_3_dif);$i0++)
      for($i1=0;$i1<count($Psi0_1_2_xx1_2_3_dif[0]);$i1++)
          for($j0=0;$j0<count($Phi0_1_2_[0]);$j0++)
              $Psi0_1_2_xx1_2_3_dif[$i1][$i0] += $Phi0_1_2_[$i1][$i0][$j0];
  for($i0=0;$i0<count($Phi1_2_3_);$i0++)
      for($i1=0;$i1<count($Phi1_2_3_[0]);$i1++)
          for($i2=0;$i2<count($Phi1_2_3_[0][0]);$i2++)
              $Phi1_2_3_[$i2][$i1][$i0] *= $Psi0_1_2_xx1_2_3_dif[$i1][$i0];
  $P_0=array_fill(0,2,0.0);
  for($i0=0;$i0<count($P_0);$i0++)
      for($j0=0;$j0<count($Phi0_1_2_[0]);$j0++)
          for($j1=0;$j1<count($Phi0_1_2_[0][0]);$j1++)
              $P_0[$i0] += $Phi0_1_2_[$j1][$j0][$i0];
  $sum=0.0;
  for($i0=0;$i0<count($P_0);$i0++)
    $sum+=$P_0[$i0];
  // $sum should not be equal to 0 ...
  for($i0=0;$i0<count($P_0);$i0++)
    $P_0[$i0]/=$sum;
  $res['a']=$P_0;
  $P_3=array_fill(0,2,0.0);
  for($i0=0;$i0<count($P_3);$i0++)
      for($j0=0;$j0<count($Phi1_2_3_);$j0++)
          for($j1=0;$j1<count($Phi1_2_3_[0]);$j1++)
              $P_3[$i0] += $Phi1_2_3_[$i0][$j1][$j0];
  $sum=0.0;
  for($i0=0;$i0<count($P_3);$i0++)
    $sum+=$P_3[$i0];
  // $sum should not be equal to 0 ...
  for($i0=0;$i0<count($P_3);$i0++)
    $P_3[$i0]/=$sum;
  $res['d']=$P_3;
  return $res;
}

print_r(getValue(array(
  "e" => [1,0],
  "b" => [0.25,0.75]
)));
$P1given0= [[0.7441177631461217, 0.2558822368538783], [0.7978015114947503, 0.2021984885052497]];
