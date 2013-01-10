.. _introduction:

============
Introduction
============

:Authors:   Ramon Bartl, Stefan Eletzhofer
:Date:      |today|

Problem Statement
=================

We're developing web services for a enterprise PLM system (Windchill_
PDMlink_) which uses a quite old web stack (Apache 2.0, Tomcat 6, Java 1.6,
Oracle_).  Because we need to *integrate* with the Java API the vendor
provides, we unfortunately can't deploy our web service code as *WAR*
files.

We're Python_ guys, and thus use Jython_ to develop our web applications.

We use modjy_ to drive WSGI applications as ordinary Java servlets inside
the Tomcat servlet container.  Because of this, there are several special
issues wrt. to deployment which differ from standard python deployment
strategies (pip, eggs, buildout_, fabric_) we use and know.

Deploying our code in a way which minimizes the possibilities of deployment
errors, and thus minimizes downtime is essential to our customers.

The situation is further complicated by the need of several monkey patches.

Another issue we face is to set up a runtime environment suitable for
the Java interop we need, both for production and development.

Goals
=====

- provide a single-file Jython_ package usable for deployment and
  development on both Unix and Windows platforms.

- include a base set of packages we need for all our projects.

- have all monkey patches needed in one central place for all projects.

- include a minimal set of debugging and development tools to work with.

- have the run time environment set up in a repeatable, easy way to
  minimize class path issues.

Non Goals
=========

- we do not want to provide a generic solution -- this is a highly
  opinionated setup.

Public Documentation Link
=========================

This documentation is also hosted at https://nexilesjython.readthedocs.org.

Repository and Issue Tracker
============================

:GitHub Page:  https://github.com/nexiles/nexiles.jython
:Repository:   git@github.com:nexiles/nexiles.jython.git
:Open Issues:  https://github.com/nexiles/nexiles.jython/issues?state=open

.. _Python:    http://python.org
.. _Jython:    http://jython.org
.. _Windchill: http://www.ptc.com/product/windchill/
.. _PDMlink:   http://www.ptc.com/product/windchill/pdmlink
.. _Oracle:    http://www.oracle.com/us/products/database/overview/index.html
.. _modjy:     http://opensource.xhaus.com/projects/show/modjy
.. _fabric:    http://docs.fabfile.org/en/1.5/
.. _buildout:  http://pypi.python.org/pypi/zc.buildout/

.. vim: set ft=rst tw=75 nocin nosi ai spell sw=4 ts=4 expandtab:

