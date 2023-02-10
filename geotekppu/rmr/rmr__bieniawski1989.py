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
    
    
    
    return None