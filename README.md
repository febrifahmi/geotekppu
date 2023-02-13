# GeotekPPU (geotekppu)
![Coverage](coverage.svg "Test Coverage")

A python module for geotechnic analysis.

## Usage

### Rock Mass Rating (RMR89)

Rock Mass Rating (RMR) is a rating system proposed by Bieniawski (1989) to classify rock based on five classification parameters.

```
Parameters:
-----------

r1 : strength rating
r2 : Rock Quality Designation (RQD) rating
r3 : space of discontinuity rating
r4 : condition of discontinuity rating
r5 : ground water rating

Return(s):
----------

RMR89 / rock mass rating value which consists of:
- Rating value
- Class number (I, II, III, IV, V)
- Description (Very good rock, Good rock, Fair rock, Poor rock, Very poor rock)
```

References:
-----------
Code developed base on [1]__
.. [1] Bieniawski, Z.T. 1989. Engineering rock mass classifications. New York: Wiley.

