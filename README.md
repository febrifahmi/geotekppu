# GeotekPPU (geotekppu)
![Coverage](coverage.svg "Test Coverage")

A python module for geotechnic analysis.

## Usage
### Installation

`pip install geotekppu==0.0.2`

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







References
----------

[1] Bieniawski, Z.T. 1989. Engineering rock mass classifications. New York: Wiley.

[2] B. Celada, I. Tardáguila, P. Varona, A. Rodríguez, and Z. T. Bieniawski, “Innovating Tunnel Design by an Improved Experience-based RMR System.,” Proc. World Tunn. Congr. 2014 – Tunnels a better Life, vol. 3, pp. 1–9, 2014.


