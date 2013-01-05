# -*- coding: utf-8 -*-
#
# File: wt_classpath.py
#
# Copyright (c) nexiles GmbH
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

__author__    = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'
__revision__  = "$Revision: $"
__version__   = '$Revision: $'[11:-2]


import os
import re
import logging

import glob

from classpath_hacker import ClassPathHacker

logger = logging.getLogger("wt_classpath")


def get_jar_files(path):
    """get_jar_files(path) -> sequence

    Fetch all jar files from the given path.  Filter out jython jar
    files.
    """
    def _(path):
        return re.match(".*jython.*.jar", path) is None

    return filter(_, glob.glob(os.path.join(path, "*.jar")))


def set_windchill_classpath(WT_HOME):
    """set_windchill_classpath(WT_HOME) -> None

    Uses the ClassPathHacker to dynamically set the JVM classpath
    to the given WT_HOME.

    :param WT_HOME: the Windchill install home

    :returns: None
    """
    h = ClassPathHacker()

    jars_added = {}

    for d in map(lambda x: os.path.join(WT_HOME, x), ["codebase", "codebase/lib", "codebase/WEB-INF/lib"]):
        logger.info("Adding jar files from '%s'" % d)
        for jarfile in get_jar_files(d):
            p = os.path.basename(jarfile)
            if p not in jars_added:
                logger.debug("Adding jar: %s" % jarfile)
                jars_added[p] = os.path.dirname(jarfile)
                h.addFile(jarfile)
            else:
                logger.warn("Duplicate jar file: %s (first load from %s)" % (jarfile, jars_added[p]))


def main():
    WT_HOME = os.environ.get("WT_HOME")
    assert WT_HOME, "WT_HOME not set"
    set_windchill_classpath(WT_HOME)

if __name__ == '__main__':
    main()

# vim: set ft=python ts=4 sw=4 expandtab :
