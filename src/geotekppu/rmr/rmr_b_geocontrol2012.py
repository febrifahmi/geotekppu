"""
Copyright (2023) Febri Fahmi Hakim (fahmi_fafa@yahoo.com) and Daru Jaka Sasangka (darujakasasangka@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# change kg/cm2 to MPa
convfactor = 0.0980665

def rmr_ucs(strength):
    """
    RMR(1) Uniaxial Compressive Strength of intact rock.

    Parameters:
    -----------

    - strength: ucs of intact rock (in kg/cm2, for consistency it will be converted automatically to MPa)

    Return:
    -------

    val_rmr_ucs: rating value of RMR(1) based on table by Geocontrol(2012)


    """
    val_rmr_ucs = 0
    
    if strength > (2500*convfactor):
        val_rmr_ucs = 15
    elif strength >= (1000*convfactor) and strength <= (2500*convfactor):
        val_rmr_ucs = 12
    elif strength >= (500*convfactor) and strength < (1000*convfactor):
        val_rmr_ucs = 7
    elif strength >= (250*convfactor) and strength < (500*convfactor):
        val_rmr_ucs = 4
    elif strength >= (50*convfactor) and strength < (250*convfactor):
        val_rmr_ucs = 2
    elif strength >= (10*convfactor) and strength < (50*convfactor):
        val_rmr_ucs = 1
    elif strength < (10*convfactor):
        val_rmr_ucs = 0

    return val_rmr_ucs


def rmr_rqd_spacing(joints):
    """
    RMR(2+3) RQD and spacing of joints.

    Parameters:
    -----------

    - joints: joints per meter

    Return:
    -------

    val_rmr_2_3: rating value of RMR(2+3)


    """
    val_rmr_2_3 = 0
    if joints == 0:
        val_rmr_2_3 = 40
    elif joints == 1:
        val_rmr_2_3 = 34
    elif joints == 2:
        val_rmr_2_3 = 31
    elif joints == 3:
        val_rmr_2_3 = 29
    elif joints == 4:
        val_rmr_2_3 = 28
    elif joints == 5:
        val_rmr_2_3 = 27
    elif joints == 6:
        val_rmr_2_3 = 26
    elif joints == 7:
        val_rmr_2_3 = 25
    elif joints == 8:
        val_rmr_2_3 = 24
    elif joints == 9:
        val_rmr_2_3 = 23
    elif joints == 10:
        val_rmr_2_3 = 22
    elif joints == 11:
        val_rmr_2_3 = 21
    elif joints == 12:
        val_rmr_2_3 = 20
    elif joints == 13:
        val_rmr_2_3 = 19
    elif joints == 14:
        val_rmr_2_3 = 18
    elif joints == 15:
        val_rmr_2_3 = 17
    elif joints == 16:
        val_rmr_2_3 = 17
    elif joints == 17:
        val_rmr_2_3 = 16
    elif joints == 18:
        val_rmr_2_3 = 15
    elif joints == 19:
        val_rmr_2_3 = 14
    elif joints == 20:
        val_rmr_2_3 = 14
    elif joints == 21:
        val_rmr_2_3 = 13
    elif joints == 22:
        val_rmr_2_3 = 13
    elif joints == 23:
        val_rmr_2_3 = 12
    elif joints == 24:
        val_rmr_2_3 = 12
    elif joints == 25:
        val_rmr_2_3 = 11
    elif joints == 26:
        val_rmr_2_3 = 11
    elif joints == 27:
        val_rmr_2_3 = 10
    elif joints == 28:
        val_rmr_2_3 = 10
    elif joints == 29:
        val_rmr_2_3 = 9
    elif joints == 30:
        val_rmr_2_3 = 9
    elif joints == 31:
        val_rmr_2_3 = 9
    elif joints == 32:
        val_rmr_2_3 = 8
    elif joints == 33:
        val_rmr_2_3 = 8
    elif joints == 34:
        val_rmr_2_3 = 7
    elif joints == 35:
        val_rmr_2_3 = 7
    elif joints == 36:
        val_rmr_2_3 = 7
    elif joints == 37:
        val_rmr_2_3 = 6
    elif joints == 38:
        val_rmr_2_3 = 6
    elif joints == 39:
        val_rmr_2_3 = 6
    elif joints == 40:
        val_rmr_2_3 = 5
    elif joints == 41:
        val_rmr_2_3 = 4
    elif joints == 42:
        val_rmr_2_3 = 3
    elif joints == 43:
        val_rmr_2_3 = 3
    elif joints == 44:
        val_rmr_2_3 = 2
    elif joints == 45:
        val_rmr_2_3 = 2
    elif joints == 46:
        val_rmr_2_3 = 1.5
    elif joints == 47:
        val_rmr_2_3 = 1
    elif joints == 48:
        val_rmr_2_3 = 1
    elif joints == 49:
        val_rmr_2_3 = 0.5
    elif joints == 50:
        val_rmr_2_3 = 0

    return val_rmr_2_3


def rmrb(rmr_ucs, rmr_rqd_spacing, discontinuity, groundwater):
    """
    RMRb - Rock Mass Rating basic for classifying rock mass as proposed by Geocontrol (2012) after Bieniawski (1989).

    Parameters:
    -----------

    - rmr_ucs: rating of Uniaxial Compressive Strength rating of intact rock
    - rmr_rqd_spacing: rating of RMR RQD and spacing of joints
    - discontinuity: discontinuity condition as proposed in Bieniawski (1989) (see discontinuity_class() in rmr_bieniawski1989.py)
    - groundwater: groundwater condition (see r5() in rmr_bieniawski1989.py)

    Return:
    -------

    __rmrb: RMRb rating value

    """
    __rmrb = rmr_ucs + rmr_rqd_spacing + discontinuity + groundwater
    return __rmrb