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

import os

# Provide to copy a content of a file in another file (using buffer and a limit to copy)
def __copyInFile(iF, oF, buffersize=1024, tocopy = 0):
    copied = 0
    i = 0
    while True:
        i += 1
        elsetocpy = tocopy - copied
        # free to copy all
        if (elsetocpy - buffersize > 0) or (tocopy == 0):
            tmp = iF.read(buffersize)
            if tmp == b'':
                if i == 1:
                    return False
                else:
                    return True
            else:
                oF.write(tmp)
                copied += buffersize
        # last data to copy
        else:
            tmp = iF.read(elsetocpy)
            if tmp == b'':
                if i == 1:
                    return False
                else:
                    return True
            else:
                oF.write(tmp)
                return True

# Split files
def split(inFileSrc, output, splitIn):
    splitNumber = 1
    try:
        inFile = open(inFileSrc, 'rb');
    except FileNotFoundError:
        print('Error: the file %s does not exists. Exiting...' % (inFileSrc))
        exit()
    while True:
        if output == None:
            outFile = open(inFileSrc + '.' + str('%03d' % (splitNumber)), 'wb')
        else:
            outFile = open(os.path.join(output, os.path.basename(inFileSrc)) + '.' + str('%03d' % (splitNumber)), 'wb')
        if not __copyInFile(inFile, outFile, 1024, splitIn):
            outFile.close()
            if output == None:
                os.remove(inFileSrc + '.' + str('%03d' % (splitNumber)))
            else:
                os.remove(os.path.join(output, os.path.basename(inFileSrc)) + '.' + str('%03d' % (splitNumber)))
            break
        else:
            outFile.close()
            splitNumber += 1

# Join files
def join(firstFileIn, output):
    firstFileInE = firstFileIn[:-3]
    outFileSrc = firstFileInE[:-1]
    joinNumber = 1
    if output != None:
        outFileSrc = os.path.join(output, os.path.basename(outFileSrc))
    outFile = open(outFileSrc, 'wb')
    while True:
        try:
            inFile = open(firstFileInE + str('%03d' % (joinNumber)), 'rb')
            __copyInFile(inFile, outFile, 1024, 0)
            #outFile.write(inFile.read())
            inFile.close()
            joinNumber += 1
        except FileNotFoundError:
            if joinNumber <= 1:
                print('Error: the file %s.001 does not exists. Exiting...' % (firstFileIn))
            outFile.close()
            return
