# GeotekPPU (geotekppu)
![Coverage](coverage.svg "Test Coverage")

A python module for geotechnic analysis.

## Usage
### Installation

`pip install geotekppu`
### How to use

`from geotekppu import *`

### Rock Mass Rating (RMR89)

Rock Mass Rating (RMR) is a rating system proposed by Bieniawski (1989) to classify rock based on five classification parameters.

This Python module is developed based on [1].

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

