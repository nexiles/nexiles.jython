# -*- coding: utf-8 -*-
#
# File: nxipython.py
#
# Copyright (c) Nexiles GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__author__ = 'Ramon Bartl <ramon.bartl@nexiles.de>'
__docformat__ = 'plaintext'

import os
import sys

if __name__=="__main__":

    if "IPYTHONDIR" not in os.environ:
        ipython_dir = os.path.join(sys.prefix, "nexiles_ipython_profile")
        print "Setting IPYTHONDIR to default: %s " % ipython_dir
        os.environ["IPYTHONDIR"] = ipython_dir

    if "WT_HOME" in os.environ:
        print "Windchill shell detected -- adding CLASSPATH to python path."

        for p in os.environ.get("CLASSPATH", "").split(os.pathsep):
            sys.path.append(p)

    from IPython.Shell import IPShellEmbed
    sh = IPShellEmbed()
    sys.exit(sh())

# vim: set ft=python ts=4 sw=4 expandtab :
