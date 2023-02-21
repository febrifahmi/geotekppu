"""
Copyright (2023) Febri Fahmi Hakim (fahmi_fafa@yahoo.com) and Daru Jaka Sasangka (darujakasasangka@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import math

def f0(strike_orientation, dip_angle):
    """
    F0 is adjustment factor for the orientation of tunnel axis with regard to main set of discontinuities.

    Parameters:
    -----------

    - strike_orientation: orientation of strike to tunnel axis ('dwd' or drive with dip, 'dad' or drive against dip, 'parallel', 'irrespective') (type: String)
    - dip_angle: dip angle (dwd, dad, parallel: 45-90 or 20-45, irrespective: 0-20)

    Return:
    -------

    val_f0: value of F0 / adjustment factor (always negative, otherwise 0)

    """
    val_f0 = 0
    if strike_orientation == "dwd":
        if dip_angle >= 20 and dip_angle < 45:
            val_f0 = -2
        elif dip_angle >= 45 and dip_angle <=90:
            val_f0 = 0
        elif dip_angle < 20:
            val_f0 = None
        elif dip_angle > 90:
            val_f0 = None
    elif strike_orientation == "dad":
        if dip_angle >= 20 and dip_angle < 45:
            val_f0 = -10
        elif dip_angle >= 45 and dip_angle <=90:
            val_f0 = -5
        elif dip_angle < 20:
            val_f0 = None
        elif dip_angle > 90:
            val_f0 = None
    elif strike_orientation == "parallel":
        if dip_angle >= 20 and dip_angle < 45:
            val_f0 = -5
        elif dip_angle >= 45 and dip_angle <=90:
            val_f0 = -12
        elif dip_angle < 20:
            val_f0 = None
        elif dip_angle > 90:
            val_f0 = None
    elif strike_orientation == "irrespective":
        if dip_angle >= 0 and dip_angle <= 20:
            val_f0 = -5
        elif dip_angle > 20:
            val_f0 = None
    return val_f0


def f_excavation(rmrb):
    """
    Adjusment factor for RMR considering excavation method (Tunneling Bore Method/TBM or Drill and Blast/D+B).

    Parameters:
    -----------

    - rmrb: RMRb rating value before adjustments (for rmrb > 40 and rmrb < 40)

    Return:
    -------

    val_fe: value of adjustments factor based on excavation method

    """
    val_fe = 0
    if rmrb < 40 and rmrb >= 0:
        val_fe = 1 + (2 * (rmrb / 100)**2)
    elif rmrb >= 40 and rmrb <= 100:
        val_fe = 1.32 - (math.sqrt(rmrb-40)/25)
    return val_fe


def ice(rmrb,ucs,k0,H,F):
    """
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

    """
    val_ice = 0
    e = 2.71828183
    if k0 <= 1:
        val_ice = ((3704*ucs*(e**((rmrb-100)/24)))/((3-k0)*H))*F
    elif k0 >1:
        val_ice = ((3704*ucs*(e**((rmrb-100)/24)))/(((3*k0)-1)*H))*F
    return val_ice


def f_stresstrain(ice):
    """
    Adjustment factor of stress-strain based on "Índice de Comportamiento Elástico" (ICE) value.


    Parameters:
    -----------

    - ice: "Índice de Comportamiento Elástico" (ICE) value.


    Return:
    -------

    val_fs: adjustment factor for stress-strain.

    """
    val_fs = 0
    if ice < 15:
        val_fs = 1.3
    elif ice >= 15 and ice < 70:
        val_fs = (2.3*math.sqrt((100-ice)))/(7.1+math.sqrt((100-ice)))
    elif ice >= 70:
        val_fs = 1

    return val_fs


def rmrb_adj(rmrb,f0):
    return rmrb + f0


def rmr14(rmrb_adj, val_fe, val_fs):
    __rmr14 = rmrb_adj * val_fe * val_fs
    return __rmr14