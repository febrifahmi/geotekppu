# GeotekPPU (geotekppu)
![Coverage](coverage.svg "Test Coverage")

A python module for geotechnic analysis.

## Usage
### Installation

`pip install geotekppu`

### How to use

`from geotekppu import *`


This Python module is developed based on [1], [2].

### Rock Mass Rating (RMR89)

Rock Mass Rating (RMR) is a rating system proposed by Bieniawski (1989) to classify rock based on five classification parameters.


```
Parameters:
-----------

r1 : strength rating
r2 : Rock Quality Designation (RQD) rating
r3 : space of discontinuity rating
discontinuity_class : condition of discontinuity rating
r5 : ground water rating

Return(s):
----------

RMR89 / rock mass rating value which consists of:
- Rating value
- Class number (I, II, III, IV, V)
- Description (Very good rock, Good rock, Fair rock, Poor rock, Very poor rock)
```

```
Function r1:
r1(idx, value)


Strength of intact rock material rating.

Parameters:
-----------

idx : selected index either 'pls' for point-loads strength or 'ucs' for uniaxial compressive strength
value : strength of intact rock material (in MPa)

Return:
-------

val_r1 : rating value of strength of rock

```

```
Function r2:
r2(drillcoreRQD)


Drill core RQD rating.

Parameter:
----------

drillcoreRQD : drill core quality or rock quality designation (in percent)

Return:
-------

val_r2 : RQD rating

```

```
Function r3:
r3(spacing)


Space of discontinuity rating.

Parameters:
-----------

Value of rock spacing : spacing of rock (in m, float)

Return:
=======

val_r3 : space of discontinuity rating 

```

```
Function discontinuity_class:
discontinuity_class(dl, sep, rough, gouge, weather)


Classification of discontinuity condition.

Parameters:
-----------

- dl: discontinuity length (persistence) in m (<1m; 1-3m; 3-10m; 10-20m; >20m) (type: Int)
- sep: separation (aperture) in mm (None; <0.1mm; 0.1-1.0mm; 1-5mm; >5mm) (type: None, Float)
- rough: roughness (very_rough; rough; slightly_rough; smooth; slickensided) (type: String)
- gouge: infilling (None; hl<5; hl>5; sl<5; sl>5) (type: None, String)
- weather: weathering (unweathered; slightly_weathered; moderately_weathered; highly_weathered; decomposed) (type: String)

Return:
-------

totalrating: total rating calculated from five parameters of discontinuity condition

```

```
Groundwater condition.

Parameters:
-----------

inflow - inflow per 10 m tunnel length (i/m)
wpress - joint water pressure / major principal 
cond - general conditions (dry, damp, wet, dripping, or flowing)

Return:
-------

val_r5 : groundwater rating

```


### Rock Mass Rating basic (RMRb)

RMRb or RMR basic is an improvement of RMR system by introducing improvement in rating of RQD and joint spacing, as proposed by Geocontrol (2012) as cited in Celada et.al (2014).

```
RMR(1) Uniaxial Compressive Strength of intact rock.

Parameters:
-----------

- strength: ucs of intact rock (in kg/cm2, for consistency it will be converted automatically to MPa)

Return:
-------

val_rmr_ucs: rating value of RMR(1) based on table by Geocontrol(2012)

```

```
RMR(2+3) RQD and spacing of joints.

Parameters:
-----------

- joints: joints per meter

Return:
-------

val_rmr_2_3: rating value of RMR(2+3)

```

```

RMRb - Rock Mass Rating basic for classifying rock mass as proposed by Geocontrol (2012) after Bieniawski (1989).

Parameters:
-----------

- rmr_ucs: rating of Uniaxial Compressive Strength rating of intact rock
- rmr_rqd_spacing: rating of RMR RQD and spacing of joints
- discontinuity: discontinuity condition as proposed in Bieniawski (1989) (see discontinuity_class() in rmr_bieniawski1989.py)
- groundwater: groundwater condition (see r5() in rmr_bieniawski1989.py)

Return:
-------

__rmrb: RMRb rating value

```

### Rock Mass Rating 2014 (RMR14)

RMR14 is an improvement of RMR system by introducing several adjustment factors, namely f0 (adjustment factor for the orientation of tunnel axis with regard to main set of discontinuities), fe (adjustment factor considering excavation method (Tunneling Bore Method/TBM or Drill and Blast/D+B)), and fs (adjustment factor of stress-strain based on "Índice de Comportamiento Elástico" (ICE) value)

```

F0 is adjustment factor for the orientation of tunnel axis with regard to main set of discontinuities.

Parameters:
-----------

- strike_orientation: orientation of strike to tunnel axis ('dwd' or drive with dip, 'dad' or drive against dip, 'parallel', 'irrespective') (type: String)
- dip_angle: dip angle (dwd, dad, parallel: 45-90 or 20-45, irrespective: 0-20)

Return:
-------

val_f0: value of F0 / adjustment factor (always negative, otherwise 0)

```

```

Adjusment factor for RMR considering excavation method (Tunneling Bore Method/TBM or Drill and Blast/D+B).

Parameters:
-----------

- rmrb: RMRb rating value before adjustments (for rmrb > 40 and rmrb < 40)

Return:
-------

val_fe: value of adjustments factor based on excavation method

```

```

"Índice de Comportamiento Elástico" (ICE) as proposed by Bieniawski and Celada (2011).

Parameters:
-----------

- rmrb: value of RMRb
- ucs: uniaxial compressive strength of intact rock (in MPa)
- k0: ratio of the horizontal to vertical virgin stress 
- H: tunnel depth (in meter)
- F: shape coefficient (circular tunnel d = 6 m -> F 1.3 ; circular tunnel d = 10 m -> F 1.0 ; coventional tunnel 14 m wide -> F 0.75 ; caverns 25 m wide x 60 m high -> F 0.55)


Return:
-------

val_ice: value of ICE

```

```

Adjustment factor of stress-strain based on "Índice de Comportamiento Elástico" (ICE) value.


Parameters:
-----------

- ice: "Índice de Comportamiento Elástico" (ICE) value.


Return:
-------

val_fs: adjustment factor for stress-strain.

```

### Rock Mass Rating HLW 

Rock Mass Rating adjustment on very deep excavation work (400 - 600m) usually used for dangerous waste disposal.


```
Adjusted R1 (adjusted uniaxial compressive rock mass strength incorporating the influence of ground water weakening and temperature environment on deep located excavation project). 

The equation of adjusted R1 proposed by Tong et.al (2022) is:

if strength (x) <= 250 MPa -> R1 = ((0.6343*math.log(x,10)) - 0.3627)
if strength (x) > 250 -> R1 = 15

Parameters:
-----------

- strength: uniaxial compressive strength test result of intact rock material/rock mass strength (in MPa)

Return:
-------

val_r1_adj: rating value of r1 (adjusted) as a continuous rating
```

```
Adjusted R2 - adjustment of rock quality designation rating.

Parameters:
-----------

- rqd: RQD rating/value.

Return:
-------

val_r2_adj: rating value of r2 (adjusted) as a continuous rating
```

```
Adjusted R3 - adjustment of rating value based on joint spacing.

Parameters:
-----------

- spacing: space of discontinuity

Return:
-------

val_r3_adj: value of r3 adjusted.
```

```
Adjustment rating for tunnel, foundation and slope based of favorability.

Parameters:
-----------

- cat: category (tunnel, foundation, slope) (type String)
- favorability: favorability opstion (vfav -> very favorable; fav -> favorable; fair; unfav -> unfavorable; vunfav: very unfavorable)

Return:
-------

val_r6: rating value of R6
```

```
Geostress correction / strength-stress ratio index / in-situ stress modification index (R7) as proposed in Tong et.al (2022) (a ration to measure the risk of rock bursts).
    Denoted by the equation:

        R7 = Sum of (Ri x Percentage of (i))

        Where Ri for specific rock burst grade:
        I (no rock burst) --> Ri = 0
        II (slight rock burst) --> Ri = -4
        III (moderate rock burst) --> Ri = -8
        IV (severe rock burst) --> Ri = -12

Parameters:
-----------

- Ri: score of Ri based on rock burst grade
- Per(i): percentage of different rock burst grade

Return:
-------

val_r7: value of R7 (sum of (ri * per_i)) from all data
```

```
Rock Mass Permeability Index as main factor influence the water seepage in rocks material.

    This value defined as:

        R8 = -12 x (1 - Perm(<=10^-9m/s))

Parameters:
-----------

- perm_co: coefficient of permeability value and it should within the range <=10^-9 m/s. If permeability coefficient value == <=10^-9 m/s == 1, then R8 = -12 x (1-1) = 0. Otherwise, when permeability coefficient value == <=10^-9 m/s == 0, R8 is -12. The coefficient is between 0 and 1.


Return:
-------

val_r8: value of R8
```

```
The gorundwater chemistry index as proposed by Tong et.al (2022). 

Parameters:
-----------

- pH: pH (acidity)
- tds: total dissolved solids (g/L)
- cl-: non/negatively charged chlorine (g/L)

Return:
-------

val_r9: value of R9
```




References
----------

[1] Bieniawski, Z.T. 1989. Engineering rock mass classifications. New York: Wiley.

[2] B. Celada, I. Tardáguila, P. Varona, A. Rodríguez, and Z. T. Bieniawski, “Innovating Tunnel Design by an Improved Experience-based RMR System.,” Proc. World Tunn. Congr. 2014 – Tunnels a better Life, vol. 3, pp. 1–9, 2014.

[3] Y. Tong, Y. Yue, Z. Huang, L. Zhu, Z. Li, and W. Zhang, “Modified RMR Rock Mass Classification System for Preliminary Selection of Potential Sites of High-Level Radioactive Waste Disposal Engineering,” Sustain., vol. 14, no. 23, pp. 1–17, 2022, doi: 10.3390/su142315596.


How to cite
-----------

```
@software{Sasangka_GeotekPPU_A_python_2023,
author = {Sasangka, Daru Jaka and Hakim, Febri Fahmi},
month = {2},
title = {{GeotekPPU: A python module for geotechnic analysis}},
url = {https://github.com/febrifahmi/geotekppu},
version = {0.0.2},
year = {2023}
}
```