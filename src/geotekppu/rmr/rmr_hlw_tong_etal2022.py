"""
Copyright (2023) Febri Fahmi Hakim (fahmi_fafa@yahoo.com) and Daru Jaka Sasangka (darujakasasangka@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import math

def AdjustedR1ucs(strength):
    """
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

    """
    val_r1_adj = 0
    if strength <= 250:
        val_r1_adj = 10**((0.6343*math.log(strength,10))-0.3627)
    elif strength > 250:
        val_r1_adj = 15
    return round(val_r1_adj,4)


def AdjustedR2(rqd):
    """
    Adjusted R2 - adjustment of rock quality designation rating.

    Parameters:
    -----------

    - rqd: RQD rating/value (0-100).

    Return:
    -------

    val_r2_adj: rating value of r2 (adjusted) as a continuous rating

    """
    val_r2_adj = 0
    if rqd < 100:
        val_r2_adj = (0.1958*rqd) + 0.6484
    elif rqd == 100:
        val_r2_adj = 20
    else:
        val_r2_adj = None
    if val_r2_adj != None:
        return round(val_r2_adj,4)
    else:
        return val_r2_adj


def AdjustedR3(spacing):
    """
    Adjusted R3 - adjustment of rating value based on joint spacing.

    Parameters:
    -----------

    - spacing: space of discontinuity

    Return:
    -------

    val_r3_adj: value of r3 adjusted.

    """
    val_r3_adj = 0
    if spacing < 2:
        val_r3_adj = 10**((0.1799*((math.log(spacing,10))**3)) + (0.3834*((math.log(spacing,10))**2)) + (0.4462*math.log(spacing,10)) + 1.125)
    elif spacing >= 2:
        val_r3_adj = 20
    else:
        val_r3_adj = None
    return round(val_r3_adj,4)


# R4, R5, R6 is the same with the traditional or modified RMR system (no adjustment) 
# 

def CalcR6(cat,favorability):
    """
    Adjustment rating for tunnel, foundation and slope based of favorability.

    Parameters:
    -----------

    - cat: category (tunnel, foundation, slope) (type String)
    - favorability: favorability opstion (vfav -> very favorable; fav -> favorable; fair; unfav -> unfavorable; vunfav: very unfavorable)

    Return:
    -------

    val_r6: rating value of R6

    """
    val_r6 = 0
    if cat == "tunnel":
        if favorability == "vfav":
            val_r6 = 0
        elif favorability == "fav":
            val_r6 = -2
        elif favorability == "fair":
            val_r6 = -5
        elif favorability == "unfav":
            val_r6 = -10
        elif favorability == "vunfav":
            val_r6 = -12
    elif cat == "foundation":
        if favorability == "vfav":
            val_r6 = 0
        elif favorability == "fav":
            val_r6 = -2
        elif favorability == "fair":
            val_r6 = -7
        elif favorability == "unfav":
            val_r6 = -15
        elif favorability == "vunfav":
            val_r6 = -25
    elif cat == "slope":
        if favorability == "vfav":
            val_r6 = 0
        elif favorability == "fav":
            val_r6 = -5
        elif favorability == "fair":
            val_r6 = -25
        elif favorability == "unfav":
            val_r6 = -50
        elif favorability == "vunfav":
            val_r6 = -60
    return val_r6

def CalcR7(ri,per_i):
    """
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

    """
    val_r7 = ri * per_i
    return val_r7 


def CalcR8(perm_co):
    """
    Rock Mass Permeability Index as main factor influence the water seepage in rocks material.

    This value defined as:

        R8 = -12 x (1 - Perm(<=10^-9m/s))

    Parameters:
    -----------

    - perm_co: coefficient of permeability value and it should within the range <=10^-9 m/s. If permeability coefficient value == <=10^-9 m/s == 1, then R8 = -12 x (1-1) = 0. Otherwise, when permeability coefficient value == <=10^-9 m/s == 0, R8 is -12. The coefficient is between 0 and 1.


    Return:
    -------

    val_r8: value of R8

    """
    val_r8 = -12 * (1 - perm_co)
    return round(val_r8,2)


def CalcR9(pH, tds, cl):
    """
    The gorundwater chemistry index as proposed by Tong et.al (2022). 

    Parameters:
    -----------

    - pH: pH (acidity)
    - tds: total dissolved solids (g/L)
    - cl-: non/negatively charged chlorine (g/L)

    Return:
    -------

    val_r9: value of R9

    """
    val_r9 = 0
    if pH > 6 and pH < 10 and tds < 50 and cl < 20:
        val_r9 = 0
    elif pH > 6 and pH < 10 and tds < 50 and cl >= 20:
        val_r9 = -4
    elif pH > 6 and pH < 10 and tds >= 50 and cl < 20:
        val_r9 = -4
    elif (pH <= 6 or pH >= 10) and tds < 50 and cl < 20:
        val_r9 = -4
    elif (pH <= 6 or pH >= 10) and tds >= 50 and cl < 20:
        val_r9 = -8
    elif (pH <= 6 or pH >= 10) and tds < 50 and cl >= 20:
        val_r9 = -8
    elif (pH <= 6 or pH >= 10) and tds >= 50 and cl >= 20:
        val_r9 = -8
    else:
        val_r9 = None
    return val_r9