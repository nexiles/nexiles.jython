# -*- coding: utf-8 -*-

__docformat__ = 'plaintext'
__fabric__ = '1.5.1'

import os

from fabric.api import task
from fabric.api import local
from fabric.api import settings
from fabric.api import lcd
from fabric.api import prefix
from fabric.utils import abort

# JYTHON_HOME must be unset!
if "JYTHON_HOME" in os.environ:
    del os.environ["JYTHON_HOME"]

NXJYTHON_VERSION       = "0.5dev"
DEFAULT_JYTHON_VERSION = "2.5.3"
DEFAULT_BASENAME       = "jython-nx"


def get_jython_home(version=DEFAULT_JYTHON_VERSION):
    JYTHON_HOME = "/usr/local/Cellar/jython/%s/libexec" % version

    if not os.path.exists(JYTHON_HOME):
        abort("Can't locate jython.jar in %s" % JYTHON_HOME)

    return JYTHON_HOME


def get_dist_dir(version=DEFAULT_JYTHON_VERSION):
    dropbox   = os.path.expanduser("~/Dropbox")
    return os.path.join(dropbox, "dist", "nexiles.jython", "nexiles.jython-%s-%s" % (version, NXJYTHON_VERSION))


def get_package_name(version, basename=DEFAULT_BASENAME):
    return "%s-%s-%s" % (basename, version, NXJYTHON_VERSION)


@task
def virtualenv(name="venv", version=DEFAULT_JYTHON_VERSION):
    """ build a jython virtualenv
    """
    # clean out any previous built virtualenvs
    local("rm -rf %s" % name)

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
        local("pip install --download-cache pip-cache -r %s" % requirements)


@task
def install_ipython(venv="venv"):
    """ activates and installs requirements
    """
    with prefix("source venv/bin/activate"):
        local("pip install --download-cache pip-cache git+git://github.com/seletz/ipython.git@0.10.2-jython#egg=ipython")


@task
def jython(version=DEFAULT_JYTHON_VERSION):
    """launches a REPL with the **local** jython"""
    package_name = get_package_name(version) + ".jar"
    local("java -jar build/%s -mnxipython" % package_name)


@task
def nxjython(version=DEFAULT_JYTHON_VERSION):
    """ nxjython -- create a nexiles jython jar.

    The jython jar file will be standalonene -- it contains all the
    standard library and the packages which are installed in the local
    virtual env 'venv'.
    """

    jython_home = get_jython_home(version=version)

    package_name = get_package_name(version) + ".jar"

    # copy jython.jar
    local("cp %s/jython.jar ." % jython_home)

    # copy std Lib dir
    local("cp -r %s/Lib ." % jython_home)

    # Copy nexiles specific scripts
    local("cp src/*.py Lib")

    # delete site-packages
    with lcd("Lib"):

        # clean site-packages
        local("rm -rf site-packages/*")

        # remove unit tests
        local("rm -rf test")

        # copy site packages from venv to Lib

        local("cp -r ../venv/Lib/site-packages/* ./site-packages")

    # compile stuff
    with settings(warn_only=True):
        local("java -jar jython.jar -m compileall Lib")

    # package new package
    local("cp jython.jar %s" % package_name)
    local("zip -r %s Lib" % package_name)

    # test
    local("rm -rf Lib jython.jar")
    local("java -jar %s -c 'import flask; print flask.__file__'" % package_name)

    # move to build directory
    local("mkdir -p build")
    local("mv %s build" % package_name)


@task
def full_monty(version=DEFAULT_JYTHON_VERSION):
    """ full build run

    Build Virtualenv, install requirements, instal ipython, build jython jar
    """

    # clean stuff from previous runs
    clean()

    # build virtual env
    virtualenv(version=version)

    # install minimal requirements
    install_requirements()
    install_ipython()

    # build nx jython jar file
    nxjython(version=version)


@task
def dist(version=DEFAULT_JYTHON_VERSION):
    """ copy distribution
    """

    dist_dir     = get_dist_dir()
    package_name = get_package_name(version) + ".jar"
    doc_package  = get_package_name(version, basename="%s-doc" % DEFAULT_BASENAME)

    # create dist dir
    local("mkdir -p %s" % dist_dir)

    # build the docs
    with lcd("docs"):
        local("make html")

        # copy docs to dist dir
        with lcd("_build/html"):
            local("tar czf {dist_dir}/{doc_package}.tgz .".format(dist_dir=dist_dir, doc_package=doc_package))

    # copy contents of build dir
    local("cp build/%s %s" % (package_name, dist_dir))

    # copy README
    local("cp README.md %s" % dist_dir)


@task
def install():
    """
    installs wrapper scripts
    """
    local("install bin/nxjython ~/bin")
    local("install bin/nxpip ~/bin")

@task
def clean():
    """clean up leftover files."""
    local("rm -rf Lib jython.jar cachedir")


@task
def dist_clean():
    """clean up leftover files AND all previous builds"""
    clean()
    local("rm -rf build")

# vim: set ft=python ts=4 sw=4 expandtab :
