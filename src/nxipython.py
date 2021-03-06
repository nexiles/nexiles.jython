# -*- coding: utf-8 -*-

__author__ = 'Ramon Bartl <ramon.bartl@nexiles.de>, Stefan Elethofer <se@nexiles.de>'
__docformat__ = 'plaintext'

import os
import sys

import logging


def setup_logging(level=logging.DEBUG):
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)-7s] [line %(lineno)d] %(name)s: %(message)s")


def nxipython(wtshell=False):
    """nxipython

    Call a IPython shell REPL.

    The `IPYTHONDIR` is set up to sys.prefix/nexiles_ipython_profile if not set.

    If `wtshell` is true, an attempt is made to set up the JVM class path
    suitable for Windchill hacking.

    :param wtshell: whether or not to set up a Windchill shell.
    """
    if "IPYTHONDIR" not in os.environ:
        ipython_dir = os.path.join(sys.prefix, "nexiles_ipython_profile")
        print "Setting IPYTHONDIR to default: %s " % ipython_dir
        os.environ["IPYTHONDIR"] = ipython_dir

    if wtshell and "WT_HOME" in os.environ:
        print "Windchill shell requested -- setting up JVM class loader"

        from wt_classpath import set_windchill_classpath
        set_windchill_classpath(os.environ["WT_HOME"])

    try:
        from IPython.Shell import IPShellEmbed
        sh = IPShellEmbed()
        return sh()
    except:
        import code
        return code.interact()

if __name__ == "__main__":
    setup_logging(logging.INFO)
    rc = nxipython(wtshell=True)
    sys.exit(rc)

# vim: set ft=python ts=4 sw=4 expandtab :
