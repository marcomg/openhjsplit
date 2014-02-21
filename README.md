OpenHJSplit
===========

What is it?
-----------
OpenHJSplit is a tool to join and split files. It's an open source alternativa to HJSplit and it is compatible with HJSplit. It's 100% free (Open Source) and is licensed under the GPLv3. It is written using python3 and it can run under GNU/Linux, FreeBSD, NetBSD, OpenBSD, Micro$oft Windows and Mac OS X

Features:
 * Split files
 * Join files

At the moment it only works in command line, but in the future will be a simple GUI.

How can I use it?
-----------------
Use it is very simple:
To split a file: openhjsplit -s -w 5MiB patcOfTheFileToSplit.ext
To join a file: openhjsplit -j patcOfTheFileToSplit.ext.001
The file will be joined or splitted in the same directory of the originally file.