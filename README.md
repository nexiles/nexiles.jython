nexiles.jython
==============

This is the nexiles jython toolbox.

Rationale
---------

We use jython to develop web applications which are then deployed
to a very old-style java stack.  To ease deployment for the end user,
we want to have all the dependencies in one jar file.  Unfortunately,
we cannot use a simple war file, because we need to integrate into
a java web framework.

Packages installed
------------------

The following packages are installed:

    Flask==0.9
    Jinja2==2.6
    Werkzeug==0.8.3
    simplejson==3.0.4
    wsgiref==0.1.2

Additionally a slightly hacked version of ipython for jython is installed.

Usage
-----

The included fab file should be pretty easy to read, basically you need to:

    $ mkvirtualenv nexiles.jython
    $ pip install -r requirements.txt

This will make sure you have fabric installed.  Then do:

    $ fab full_monty

This will run for several minutes and generate a jython-nx-<version>.jar.  You
should now be able to do something like:

    $ java -jar jython-nx-2.5.3.jar
    Jython 2.5.3 (2.5:c56500f08d34+, Aug 13 2012, 14:48:36)
    [Java HotSpot(TM) 64-Bit Server VM (Apple Inc.)] on java1.6.0_37
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

IPython
-------

We provide package ipython and a start module for ipython, so that you can
do:

    $ java -jar jython-nx-2.5.3.jar -mnxipython

To start IPython.  Note that the `IPYTHONDIR` is set to `sys.prefix` if unset.
