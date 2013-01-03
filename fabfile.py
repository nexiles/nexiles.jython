# -*- coding: utf-8 -*-

__docformat__ = 'plaintext'
__fabric__ = '1.3.3'

import os

from fabric.api import task
from fabric.api import local
from fabric.api import settings
from fabric.api import lcd
from fabric.api import prefix
from fabric.utils import abort
#from fabric.colors import red, green, yellow


def get_jython_home(version="2.5.3"):
    JYTHON_HOME="/usr/local/Cellar/jython/%s/libexec" % version

    if not os.path.exists(JYTHON_HOME):
        abort("Can't locate jython.jar in %s" % JYTHON_HOME)

    return JYTHON_HOME

if "JYTHON_HOME" in os.environ:
    del os.environ["JYTHON_HOME"]

@task
def virtualenv(name="venv", version="2.5.3"):
    """ build a jython virtualenv
    """
    jython_home = get_jython_home(version=version)

    # compute the full path of the current jython executable
    jython_bin = os.path.join(jython_home, "jython")

    # create virtualenv
    local("virtualenv -p %s %s" % (jython_bin, name))


@task
def install_requirements(venv="venv", requirements="requirements-jython.txt"):
    """ activates and installs requirements
    """
    with prefix("source venv/bin/activate"):
        local("pip install -r %s" % requirements)


@task
def install_ipython(venv="venv"):
    """ activates and installs requirements
    """
    with prefix("source venv/bin/activate"):
        local("pip install git+git://github.com/seletz/ipython.git@0.10.2-jython#egg=ipython")

@task
def nxjython(version="2.5.3"):
    """
    nxjython -- create a nexiles jython jar.

    The jython jar file will be standalonene -- it contains all the
    standard library and the packages which are installed in the local
    virtual env 'venv'.
    """

    jython_home = get_jython_home(version=version)

    PACKAGE_NAME="jython-nx-%s.jar" % version


    # clean stuff from previous runs
    local("rm -rf Lib jython-nx.jar jython.jar cachedir Lib_x")

    # copy jython.jar
    local("cp %s/jython.jar ." % jython_home)

    # copy std Lib dir
    local("cp -r %s/Lib ." % jython_home)

    # Copy nexiles-fu scripts
    local("cp src/*.py Lib")

    # delete site-packages
    with lcd("Lib"):

        # clean site-packages
        local("rm -rf site-packages/*")

        # copy site packages from venv to Lib

        local("cp -r ../venv/Lib/site-packages/* ./site-packages")

    # compile stuff
    with settings(warn_only=True):
        local("java -jar jython.jar -m compileall Lib")

    # package new package
    local("cp jython.jar %s" % PACKAGE_NAME)
    local("zip -r %s Lib" % PACKAGE_NAME)

    # test
    local("rm -rf Lib jython.jar")
    local("java -jar %s -c 'import flask; print flask.__file__'" % PACKAGE_NAME)

    local("cp %s /Volumes/settr-vm-nexiles/xfer" % PACKAGE_NAME)


@task
def full_monty(version="2.5.3"):
    """do everything"""

    clean()

    # build virtual env
    virtualenv(version=version)

    # install minimal requirements
    install_requirements()
    install_ipython()

    # build nx jython jar file
    nxjython(version=version)

@task
def clean():
    local("rm -rf venv Lib jython.jar cachedir")

# vim: set ft=python ts=4 sw=4 expandtab :
