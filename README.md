nexiles.jython
==============

:Version: 0.5dev
:Date:    2013-01-10

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

    Flask==0.8
    Jinja2==2.6
    Werkzeug==0.8.3
    simplejson==3.0.4
    wsgiref==0.1.2

Additionally a slightly hacked version of ipython for jython is installed.

Documentation
-------------

Please see the [documentation](https://readthedocs.org/projects/nexilesjython/)
