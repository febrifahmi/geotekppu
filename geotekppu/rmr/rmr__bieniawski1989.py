"""
Copyright (2023) Febri Fahmi Hakim (febri.fahmi@politeknikpu.ac.id) and Daru Jaka Sasangka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

def r1(idx, value):
    """
    Strength of intact rock material rating.

    Parameters:
    -----------

    idx : selected index
    value : strength of intact rock material (in MPa)

    Return:
    -------

    val_r1 : rating value of strength of rock

    """
    val_r1 = 0
    if idx == "pls":
        if value > 10:
            val_r1 = 15
        elif 10 > value and value > 4:
            val_r1 = 12
        elif 4 > value and value > 2:
            val_r1 = 7
        elif 2 > value and value > 1:
            val_r1 = 4
        else:
            print("For value lower than 1 MPa, please proceed with Uniaxial Compressive Strength Test") 
    elif idx == "ucs":
        if value > 250:
            val_r1 = 15
        elif 250 > value and value > 100:
            val_r1 = 12
        elif 100 > value and value > 50:
            val_r1 = 7
        elif 50 > value and value > 25:
            val_r1 = 4
        elif 25 > value and value > 5:
            val_r1 = 2
        elif 5 > value and value > 1:
            val_r1 = 1
        elif value < 1:
            val_r1 = 0

    return val_r1

def r2(drillcoreRQD):
    """
    Drill core RQD rating.

    Parameter:
    ----------

    drillcoreRQD : drill core quality or rock quality designation (in percent)

    Return:
    -------

    val_r2 : RQD rating

    """
    val_r2 = 0
    if 100 >= drillcoreRQD and drillcoreRQD >= 90:
        val_r2 = 20
    elif 90 >= drillcoreRQD and drillcoreRQD >= 75:
        val_r2 = 17
    elif 75 >= drillcoreRQD and drillcoreRQD >= 50:
        val_r2 = 13
    elif 50 >= drillcoreRQD and drillcoreRQD >= 25:
        val_r2 = 8
    elif drillcoreRQD < 25:
        val_r2 = 3
    return val_r2


def r3(spacing):
    """
    Space of discontinuity rating.

    Parameters:
    -----------

    Value of rock spacing : spacing of rock (in m, float)

    Return:
    =======

    val_r3 : space of discontinuity rating 

    """
    val_r3 = 0
    if spacing > 2.0:
        val_r3 = 20
    elif 2.0 >= spacing and spacing >= 0.6:
        val_r3 = 15
    elif 0.6 >= spacing and spacing >= 0.2:
        val_r3 = 10
    elif 0.2 >= spacing and spacing >= 0.06:
        val_r3 = 8
    elif spacing < 0.06:
        val_r3 = 5
    return val_r3


def r4(code):
    """
    Condition of discontinuities.

    Parameters:
    -----------

    We use code to represents condition of discontinuity in a rock material (code):
    1 - very rough surfaces, not continuous, no separation, unweathered wall rock
    2 - slightly rough surfaces, separation < 1mm, slightly weathered walls
    3 - slightly rough surfaces, separation < 1mm, highly weathered walls
    4 - slickensidd surfaces, or gouge 5mm thick, or separation 1-5mm continuous 
    5 - soft gouge > 5mm thick, or separation > 5mm continuous

    Return:
    -------

    val_r4 : condition of discontinuities rating

    """
    val_r4 = 0
    if code == 1:
        val_r4 = 30
    elif code == 2:
        val_r4 = 25
    elif code == 3:
        val_r4 = 20
    elif code == 4:
        val_r4 = 10
    elif code == 5:
        val_r4 = 0
    return val_r4


def r5(inflow, wpress, cond):
    """
    Groundwater condition.

    Parameters:
    -----------

    inflow - inflow per 10 m tunnel length (i/m)
    wpress - joint water pressure / major principal 
    cond - general conditions

    Return:
    -------

    val_r5 : groundwater rating

    """
    val_r5 = 0
    if inflow == "none" and wpress == 0 and cond == "dry":
        val_r5 = 15
    elif inflow < 10 and wpress < 0.1 and cond == "damp":
        val_r5 = 10
    elif 25 >= inflow and inflow >= 10  and 0.2 >= wpress and wpress >= 0.1 and cond == "wet":
        val_r5 = 7
    elif 125 >= inflow and inflow > 25 and 0.5 >= wpress and wpress >= 0.2 and cond == "dripping":
        val_r5 = 4
    elif inflow > 125 and wpress > 0.5 and cond == "flowing":
        val_r5 = 0
    return val_r5


def rmr89(r1, r2, r3, r4, r5):
    """
    Rock Mass Rating (RMR) value calculation as proposed by Bieniawski (1973) to classify rock mass based on 5 classification parameters.

    An implementation of [1]__.

    Features:
    ---------

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
    - Description (Very good rock, good rock, Fair rock, Poor rock, Very poor rock)

    Notes:
    ------

    References:
    -----------
    Code developed base on [1]__
    .. [1] Bieniawski, Z.T. 1989. Engineering rock mass classifications. New York: Wiley.

    """
    __rmr89 = r1 + r2 + r3 + r4 + r5 
    return __rmr89