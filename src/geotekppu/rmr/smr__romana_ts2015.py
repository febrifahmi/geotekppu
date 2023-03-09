"""
Copyright (2023) Febri Fahmi Hakim (fahmi_fafa@yahoo.com) and Daru Jaka Sasangka (darujakasasangka@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Slope Mass Rating (based on Romana. M (1985)) - Romana et.al (2015)

# define A, B, and C first
A = 0
B = 0
C = 0


def F1(ftype, dis_dd, slope_d):
    """
    Correction factor F1 which depends on parallelism (denoted by "A") between discontinuity dip direction (alpha j) and slope dip (alpha s)

    if ftype: P, then A = |alpha j - alpha s| OR absolute value of alpha j minus alpha s
    if ftype: T, the A = |alpha j - alpha s - 180| OR absolute value of alpha j minus alpha s minus 180

    Parameters:
    -----------

    - ftype: type of failure (P = planar, T = Toppling)
    - dis_dd: discontinuity dip direction
    - slope_d: slope dip


    Return:
    -------

    val_f1: value of correction factor F1

    """
    val_f1 = 0
    if dis_dd <= 360 and slope_d <=360:
        if ftype == "P":
            A = abs(dis_dd-slope_d)
            if A > 30:
                val_f1 = 0.15
            elif A <= 30 and A > 20:
                val_f1 = 0.40
            elif A <=20 and A > 10:
                val_f1 = 0.70
            elif A <= 10 and A > 5:
                val_f1 = 0.85
            elif A <= 5:
                val_f1 = 1.00

        elif ftype == "T":
            A = abs(dis_dd-slope_d-180)
            if A > 30:
                val_f1 = 0.15
            elif A <= 30 and A > 20:
                val_f1 = 0.40
            elif A <=20 and A > 10:
                val_f1 = 0.70
            elif A <= 10 and A > 5:
                val_f1 = 0.85
            elif A <= 5:
                val_f1 = 1.00
    else:
        val_f1 = None

    return val_f1


def F2(ftype, dis_dip):
    """
    Correction factor F2 related to the probability of discontinuity shear strength (B) (Romana, 1993), depends on the discontinuity dip. In case of failure type Planar: B = beta j ; in case of Toppling: B = 1.0

    Parameters:
    -----------

    - ftype: type of failure (P = planar, T = Toppling)
    - dis_dip: discontinuity dip angle


    Return:
    -------

    val_f2: value of correction factor F2
 
    """
    val_f2 = 0
    if dis_dip <= 360:
        if ftype == "P":
            if dis_dip < 20:
                val_f2 = 0.15
            elif dis_dip >= 20 and dis_dip < 30:
                val_f2 = 0.40
            elif dis_dip >= 30 and dis_dip < 35:
                val_f2 = 0.70
            elif dis_dip >= 35 and dis_dip < 45:
                val_f2 = 0.85
            elif dis_dip >= 45:
                val_f2 = 1.00
        elif ftype == "T":
            val_f2 = 1.00
    else:
        val_f2 = None
    return val_f2


def F3(ftype, slope, ddips):
    """
    Correction factor F3 indicates relationship (C) between slope (beta s) discontinuity dips (beta j) that is probability of the discontinuity to outcrop on the slope face (Romana, 1993) for planar failure (Romana, 2015)


    Parameters:
    -----------

    - ftype: type of failure (P = planar, T = Toppling)
    - slope: slope
    - ddips: discontinuity dips

    Return:
    -------

    val_f3: value of correction factor F3

    """
    val_f3 = 0
    if ftype == "P":
        C = slope - ddips
        if C <= 90:
            if C > 10:
                val_f3 = 0
            elif C <= 10 and C > 0:
                val_f3 = -6
            elif C == 0:
                val_f3 = -25
            elif C < 0 and C >= -10:
                val_f3 = -50
            elif C < - 10:
                val_f3 = -60
        else:
            val_f3 = None
    elif ftype == "T":
        C = slope + ddips
        if C <= 180:
            if C < 110:
                val_f3 = 0
            elif C >= 110 and C < 120:
                val_f3 = -6
            elif C >= 120:
                val_f3 = -25
        else:
            val_f3 = None

    return val_f3


def F4(method):
    """
    Correction factor F4 considering the excavation method.

    Parameters:
    -----------

    - method: excavation methods option ("pre": Presplitting; "sb": Smooth blasting; "ns": Natural slope; "bm": Blasting or mechanical)


    Return:
    -------

    val_f4: value of correction factor F4

    """
    val_f4 = 0
    if method == "pre":
        val_f4 = 10
    elif method == "sb":
        val_f4 = 8
    elif method == "ns":
        val_f4 = 15
    elif method == "bm":
        val_f4 = 0
    return val_f4


def SMR2015(rmrb, F1, F2, F3, F4):
    """
    Slope Mass Rating (SMR) as proposed by Romana (1985, 2015).

    Parameters:
    -----------

    - rmrb: RMR basic
    - F1: correction factor F1 regarding parallelism
    - F2: correction factor F2 regarding probability of discontinuity shear strength
    - F3: correction factor F3 regarding 

    Return:
    -------

    smr: Slope mass rating value

    """
    smr = rmrb + (F1 * F2 * F3) + F4
    return smr