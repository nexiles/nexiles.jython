============
Introduction
============

What is it?
-----------

This project provides a standalone version of jython containing the standard
library, an jython ipython interpreter and the flask framework stack
(http://flask.pocoo.org/).

Why do we need it?
------------------

Installing Jython with the dependent packages on deployment machines,
especially Windows boxes, is a major PITA. So this package can be simply used
inside a Tomcat Environment as a servlet gateway in combination with Modjy
(http://opensource.xhaus.com/projects/show/modjy).
