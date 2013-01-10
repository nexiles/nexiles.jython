# -*- coding: utf-8 -*-
#
# File: sitecustomize.py
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

# get the nexiles jython package into the path.
for index, p in enumerate(sys.path):
    if ".jar" in p:
        sys.path.insert(index+1, os.path.join(p, "site-packages"))
        break

from monkey import patch
patch()

# add WEB-INF/lib-python as site dir if we have a WT_HOME
if "WT_HOME" in os.environ:
    from site import addsitedir

    WT_HOME = os.environ["WT_HOME"]
    addsitedir(os.path.join(WT_HOME, "codebase", "WEB-INF", "lib-python"))


# vim: set ft=python ts=4 sw=4 expandtab :
