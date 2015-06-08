########################################################################
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#
#                                                                      #
# Copyright (C) 2013 by marcomg                                        #
########################################################################

def getUnitAndValue(inVar):
    inVar = str(inVar)
    number = ''
    unit = ''
    for l in inVar:
        if(l.isdigit() or l == ',' or l == '.'):
            if l == ',':
                l = '.'
            number += l
        else:
            unit += l
    number = float(number)
    return (number, unit)

def getBytes(inVar):
    tmp = getUnitAndValue(inVar)
    number = tmp[0]
    unit = tmp[1]
    del tmp
    #IS
    if(unit == 'k' or unit == 'K' or unit == 'KB'):
        return int(number * 1000)
    elif(unit == 'm' or unit == 'M' or unit == 'MB'):
        return int(number * 1000000)
    elif(unit == 'g' or unit == 'G' or unit == 'GB'):
        return int(number * 1000000000)
    elif(unit == 't' or unit == 'T' or unit == 'TB'):
        return int(number * 1000000000000)
    elif(unit == 'p' or unit == 'P' or unit == 'PB'):
        return int(number * 1000000000000000)
    elif(unit == 'e' or unit == 'E' or unit == 'EB'):
        return int(number * 1000000000000000000)
    elif(unit == 'z' or unit == 'Z' or unit == 'ZB'):
        return int(number * 1000000000000000000000)
    elif(unit == 'y' or unit == 'Y' or unit == 'YB'):
        return int(number * 1000000000000000000000000)
    #BU
    elif(unit == 'KiB'):
        return int(number * 1024)
    elif(unit == 'MiB'):
        return int(number * 1048576)
    elif(unit == 'GiB'):
        return int(number * 1073741824)
    elif(unit == 'TiB'):
        return int(number * 1099511627776)
    elif(unit == 'PiB'):
        return int(number * 1125899906842624)
    elif(unit == 'EiB'):
        return int(number * 1152921504606846976)
    elif(unit == 'ZiB'):
        return int(number * 1180591620717411303424)
    elif(unit == 'YiB'):
        return int(number * 1208925819614629174706176)
    elif(unit == '' or unit == 'b' or unit == 'B'):
        return int(number)
    else:
        print('Fatal error during conversion of %s, is an effective unit of measure? Exiting...' % (str(inVar)))
        exit()

def getHumanValue(inVar, si=True):
    inVar = int(inVar)
    #si
    if si:
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str((inVar))+'KB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'MB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'GB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'TB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'PB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'EB')
        if(inVar >= 1000):
            inVar = inVar/1000
            if(inVar < 1000):
                return(str(int(inVar))+'ZB')
        if(inVar >= 1000):
            inVar = inVar/1000
            #if(inVar < 1000):
            return(str(int(inVar))+'YB')
        else:
            return(str(int(inVar))+'B')
    #bu
    else:
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str((inVar))+'KiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'MiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'GiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'TiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'PiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'EiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            if(inVar < 1024):
                return(str(int(inVar))+'ZiB')
        if(inVar >= 1024):
            inVar = inVar/1024
            #if(inVar < 1024):
            return(str(int(inVar))+'YiB')
        else:
            return(str(int(inVar))+'B')

def optimize(inVar, si=True):
    return getHumanValue(getBytes(inVar), si)
