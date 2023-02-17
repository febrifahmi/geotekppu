# GeotekPPU (geotekppu)
![Coverage](coverage.svg "Test Coverage")

A python module for geotechnic analysis.

## Usage
### Installation

`pip install geotekppu==0.0.2`
### How to use

`from geotekppu import *`

### Rock Mass Rating (RMR89)

Rock Mass Rating (RMR) is a rating system proposed by Bieniawski (1989) to classify rock based on five classification parameters.

This Python module is developed based on [1], [2].

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

References
----------
[1] Bieniawski, Z.T. 1989. Engineering rock mass classifications. New York: Wiley.
[2] B. Celada, I. Tardáguila, P. Varona, A. Rodríguez, and Z. T. Bieniawski, “Innovating Tunnel Design by an Improved Experience-based RMR System.,” Proc. World Tunn. Congr. 2014 – Tunnels a better Life, vol. 3, pp. 1–9, 2014.

