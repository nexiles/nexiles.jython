# -*- coding: utf-8 -*-

__author__ = 'Ramon Bartl <ramon.bartl@nexiles.de>'
__docformat__ = 'plaintext'

import os
import sys

# get the nexiles jython package into the path.
for index, p in enumerate(sys.path):
    if ".jar" in p:
        site_packages_dir = os.path.join(p, "site-packages")
        sys.path.insert(index + 1, site_packages_dir)

        # also add pip and distribute
        sys.path.append(site_packages_dir + "/distribute-0.6.31-py2.5.egg")
        sys.path.append(site_packages_dir + "/pip-1.2.1-py2.5.egg")
        break

sys.add_package("org.json")
sys.add_package("org.json.simple")
sys.add_package("org.json.simple.parser")

from monkey import patch
patch()

# add WEB-INF/lib-python as site dir if we have a WT_HOME
if "WT_HOME" in os.environ:
    from site import addsitedir

    WT_HOME = os.environ["WT_HOME"]
    addsitedir(os.path.join(WT_HOME, "codebase", "WEB-INF", "lib-python"))

    if "SETUP_WT_CLASSPATH" in os.environ:
        import wt_classpath
        wt_classpath.set_windchill_classpath(WT_HOME)


# vim: set ft=python ts=4 sw=4 expandtab :
