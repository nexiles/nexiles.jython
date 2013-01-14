.. _usage:

=====
Usage
=====

Abstract
========

This document describes the basic usage of the **nexiles jython** package.

Supported Use Cases
===================

**jython shell**
    Get a REPL where you can interact with the system using Python.

**deployment**
    Deploy the package into a tomcat servlet container.

**local development**

Jython Shell
============

To call up a Jython shell manually, do::

    $ java -jar <<path-to-package>>

If you use our build packages, then this would be something like::

    $ java -jar jython-nx-2.5.3-0.3.jar

.. note:: Please refer to :ref:`building` for an explaination of the versioning scheme used.

If you want/need a IPython_ shell, use::

    $ java -jar jython-nx-2.5.3-0.3.jar -mnxipython

.. note:: Currently, the IPython shell does not work on Windows -- see
   https://github.com/nexiles/nexiles.jython/issues/1

Deployment
==========

For deployment inside a Tomcat servlet container, you need to add to your
`web.xml` file something like this::

     <servlet>
        <servlet-name>jython app</servlet-name>
        <servlet-class>com.xhaus.modjy.ModjyJServlet</servlet-class>
        <init-param>
          <param-name>log_level</param-name>
          <param-value>debug</param-value>
        </init-param>
        <init-param>
          <param-name>multithread</param-name>
          <param-value>1</param-value>
        </init-param>
        <init-param>
          <param-name>python.home</param-name>
          <param-value>WEB-INF/lib</param-value>
        </init-param>
        <init-param>
          <param-name>app_import_name</param-name>
          <param-value>my.module.app.handler</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
      </servlet>

Please refer to the modjy_ documentation for more information.

For the above to work, you must:

- place the jython package to `WEB-INF/lib`

- create a python WSGI app using e.g. Flask_ and have a WSGI handler
  available using the dotted name specified as `app_import_name` servlet
  parameter.

Local Development
=================

To aid *local* development, the package has a `site.py` included which enables
user site dirs.

To use this, you need:

- `PYTHONUSERBASE` set to a directory with your local packages or python
  `.pth` files

For local `windchill` development, you need to have:

- `WT_HOME` set in your environment
- `SETUP_WT_CLASSPATH` set


.. _IPython: http://ipython.org/
.. _modjy:   http://opensource.xhaus.com/projects/show/modjy
.. _Flask:   http://flask.pocoo.org/

.. vim: set ft=rst ts=4 sw=4 expandtab tw=78 :

