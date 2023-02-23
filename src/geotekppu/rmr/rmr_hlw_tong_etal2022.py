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
        val_r1_adj = ((0.6343*math.log(strength,10))-0.3627)
    elif strength > 250:
        val_r1_adj = 15
    return round(val_r1_adj,4)


def AdjustedR2(rqd):
    """
    Adjusted R2 - adjustment of rock quality designation rating.

    Parameters:
    -----------

    - rqd: RQD rating/value.

    Return:
    -------

    val_r2_adj: rating value of r2 (adjusted) as a continuous rating

    """
    val_r2_adj = 0
    if rqd < 250:
        val_r2_adj = (0.1958*rqd) + 0.6484
    elif rqd == 250:
        val_r2_adj = 20
    else:
        val_r2_adj = None
    return round(val_r2_adj,4)



