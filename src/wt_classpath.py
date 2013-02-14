# -*- coding: utf-8 -*-

__author__    = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'
__revision__  = "$Revision: $"
__version__   = '$Revision: $'[11:-2]

import os
import re
import logging

import glob

from classpath_hacker import ClassPathHacker

#logger = logging.getLogger("wt_classpath")


def get_jar_files(base, path):
    """get_jar_files(base, path) -> sequence

    Fetch all jar files from the given path.  Filter out jython jar
    files.
    """
    def _(path):
        return re.match(".*jython.*.jar", path) is None

    p = os.path.join(base, path)
    return filter(_, glob.glob(os.path.join(p, "*.jar")))


def set_windchill_classpath(WT_HOME):
    """set_windchill_classpath(WT_HOME) -> None

    Uses the ClassPathHacker to dynamically set the JVM classpath
    to the given WT_HOME.

    :param WT_HOME: the Windchill install home

    :returns: None
    """
    h = ClassPathHacker()

    h.addFile(os.path.join(WT_HOME, "codebase"))

    jars_added = {}

    for d in [("codebase", "lib"), ("codebase", "WEB-INF", "lib")]:
        d = os.path.join(*d)
        #logger.info("Adding jar files from '%s'" % d)
        for jarfile in get_jar_files(WT_HOME, d):
            p = os.path.basename(jarfile)
            if p not in jars_added:
                #logger.debug("Adding jar: %s" % jarfile)
                jars_added[p] = os.path.dirname(jarfile)
                h.addFile(jarfile)
            else:
                pass
                #logger.warn("Duplicate jar file: %s (first load from %s)" % (jarfile, jars_added[p]))


# vim: set ft=python ts=4 sw=4 expandtab :
