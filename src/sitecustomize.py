# -*- coding: utf-8 -*-

__author__ = 'Ramon Bartl <ramon.bartl@nexiles.de>'
__docformat__ = 'plaintext'

import os
import sys

# get the nexiles jython package into the path.
for index, p in enumerate(sys.path):
    if ".jar" in p:
        sys.path.insert(index + 1, os.path.join(p, "site-packages"))
        break

from monkey import patch
patch()

# add WEB-INF/lib-python as site dir if we have a WT_HOME
if "WT_HOME" in os.environ:
    from site import addsitedir

    WT_HOME = os.environ["WT_HOME"]
    addsitedir(os.path.join(WT_HOME, "codebase", "WEB-INF", "lib-python"))


# vim: set ft=python ts=4 sw=4 expandtab :
