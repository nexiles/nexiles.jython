.. _building:

========
Building
========

Abstract
========

This document describes the build process of the **nexiles jython** package.

The build process uses Fabric_ to automate things.

.. _Fabric:   http://fabfile.org

Prerequisites
=============

We assume you are on a Mac OSX Machine with a Jython installed using homebrew_.

To install Jython using homebrew_, do::

    $ brew install jython

This should fetch and install Jython to `/usr/local/Cellar/jython`.

.. note:: Currently teh **development** version of Jython is not supported by
   this build process, e.g. we're still stuck on 2.5.3 :p

.. _homebrew: http://mxcl.github.com/homebrew

Quickstart
==========

#. Clone the Repository::

    $ mkdir -p ~/develop/nexiles
    $ cd ~/develop/nexiles
    $ git clone git@github.com:nexiles/nexiles.jython.git

#. Create a dedicated Virtualenv.  This is just an example using the virtualenv
   wrapper tools::

    $ mkvirtualenv nexiles.jython
    $ cd nexiles.jython
    $ setvirtualenvproject  # set the project dir

#. Install the build requirements::

    (nexiles.jython)$ pip install -r requirements.txt

#. Create a standalone jython package::

    (nexiles.jython)$ fab full_monty

This should be the steps needed to create the package.  The package will be
placed in the `build` directory.

Versioning scheme used
======================

The built packages use the following name scheme::

    jython-nx-<<JYTHON_VERSION>>-<<PACKAGE_VERSION>>.jar

e.g. something like::

    jython-nx-2.5.3-0.3.jar

The current versions used by the build process are specified in the
`fabfile.py`.

Testing
=======

To test the build, activate the virtual environment and execute the `jython`
fab task::

    $ workon nexiles.jython
    (nexiles.jython)$ fab jython
    [localhost] local: java -jar build/jython-nx-2.5.3-0.3.jar -mnxipython
    Setting IPYTHONDIR to default: /Users/seletz/develop/nexiles/nexiles.jython/build/nexiles_ipython_profile
    Reading history: /Users/seletz/develop/nexiles/nexiles.jython/build/nexiles_ipython_profile/history

    In [1]:

Building the documentation
==========================

To build the docs, do::

    $ workon nexiles.jython
    (nexiles.jython)$ cd docs
    (nexiles.jython)$ make html
    (nexiles.jython)$ make preview

..  vim: set ft=rst ts=4 sw=4 expandtab tw=78 :
