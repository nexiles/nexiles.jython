=====
Usage
=====

This document describes the basic usage of this toolset.


Prerequisites
=============

We assume you are on a Mac OSX Machine with a
homebrew (http://mxcl.github.com/homebrew/)
installed version of jython.

The Jython install directory should be here::

    /usr/local/Cellar/jython


Quickstart
==========

#. Clone the Repository::

    $ mkdir -p ~/develop/nexiles
    $ cd ~/develop/nexiles
    $ git clone git@github.com:nexiles/nexiles.jython.git

#. Create a dedicated Virtualenv::

    $ mkvirtualenv nexiles.jython

#. Install the requirements::

    $ pip install -r requirements.txt

#. List fabric tasks::

   $ fab --list

#. Create a standalone jython package::

    $ fab full_monty:version=2.5.3

    .. note:: This assumes you have Jython 2.5.3 installed at
              /usr/local/Cellar/jython/2.5.3"

#. Execute the standalone jython interpreter::

    $ java -jar jython-nx-2.5.3.jar

#. Execute the standalone jython ipython interpreter::

    $ java -jar jython-nx-2.5.3.jar -m nxipython

#. Create the docs::

    $ cd docs
    $ make html
