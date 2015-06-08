#!/usr/bin/python3

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

import argparse
import libhjsplit
import libitunitsconversion

try:
    argParse = argparse.ArgumentParser(description='An open source alternative to hjsplit', prog='A file splitter and joiner')
    argParse.add_argument('-v', '--version', action='version', version='%(prog)s version 1.0')
    argParse.add_argument('-j', '--join', action='store_true', help='select if join files')
    argParse.add_argument('-s', '--split', action='store_true', help='select if split files')
    argParse.add_argument('-w', '--weight', action='store', type=str, help='the file size to split');
    argParse.add_argument('-o', '--output', action='store', type=str, help='change the default output directory');
    argParse.add_argument('patch', action='store', type=str, help='the file patch (if join the first file [with .001], if split the file to split)');
    args = argParse.parse_args()

    if args.join and args.split:
        print('Or join or split, decide. Exiting...')
        exit()

    if args.join:
        libhjsplit.join(args.patch, args.output)
    elif args.split:
        if args.weight == None:
            print('Select the weight. Exiting...')
            exit()
        libhjsplit.split(args.patch, args.output, libitunitsconversion.getBytes(args.weight))
    else:
        print('Or join or split, decide. Exiting...')
        exit()
except KeyboardInterrupt:
    print(' is caught, exiting...')
    exit()