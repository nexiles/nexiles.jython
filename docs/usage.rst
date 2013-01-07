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

.. note:: This assumes you have Jython 2.5.3 installed at /usr/local/Cellar/jython/2.5.3

#. Execute the standalone jython interpreter::

    $ java -jar jython-nx-2.5.3.jar

#. Execute the standalone jython ipython interpreter::

    $ java -jar jython-nx-2.5.3.jar -m nxipython

#. Create the docs::

    $ cd docs
    $ make html


Troubleshooting
===============

Adjusting the Memory
--------------------

Traceback::

    java.lang.OutOfMemoryError: Java heap space
            at java.util.concurrent.ConcurrentHashMap$Segment.put(ConcurrentHashMap.java:438)
            at java.util.concurrent.ConcurrentHashMap.put(ConcurrentHashMap.java:883)
            at org.python.core.PyDictionary.dict___setitem__(PyDictionary.java:181)
            at org.python.core.PyDictionary.__setitem__(PyDictionary.java:176)
            at org.python.modules.zipimport.zipimporter.readZipFile(zipimporter.java:403)
            at org.python.modules.zipimport.zipimporter.readDirectory(zipimporter.java:351)
            at org.python.modules.zipimport.zipimporter.zipimporter___init__(zipimporter.java:116)
            at org.python.modules.zipimport.zipimporter.zipimporter___init__(zipimporter.java:82)
            at org.python.modules.zipimport.zipimporter$exposed___new__.createOfType(Unknown Source)
            at org.python.core.PyOverridableNew.new_impl(PyOverridableNew.java:12)
            at org.python.core.PyType.invokeNew(PyType.java:466)
            at org.python.core.PyType.type___call__(PyType.java:1558)
            at org.python.core.PyType.__call__(PyType.java:1548)
            at org.python.core.PyObject.__call__(PyObject.java:387)
            at org.python.core.imp.getPathImporter(imp.java:423)
            at org.python.core.imp.find_module(imp.java:460)
            at org.python.core.imp.import_next(imp.java:713)
            at org.python.core.imp.import_name(imp.java:824)
            at org.python.core.imp.importName(imp.java:884)
            at org.python.core.ImportFunction.__call__(__builtin__.java:1220)
            at org.python.core.PyObject.__call__(PyObject.java:357)
            at org.python.core.__builtin__.__import__(__builtin__.java:1173)
            at org.python.core.imp.importFromAs(imp.java:978)
            at org.python.core.imp.importFrom(imp.java:954)
            at string$py.f$0(/Users/rbartl/develop/nexiles/nexiles.tools/package/tmp/Lib/string.py:529)
            at string$py.call_function(/Users/rbartl/develop/nexiles/nexiles.tools/package/tmp/Lib/string.py)
            at org.python.core.PyTableCode.call(PyTableCode.java:165)
            at org.python.core.PyCode.call(PyCode.java:18)
            at org.python.core.imp.createFromCode(imp.java:386)
            at org.python.core.util.importer.importer_load_module(importer.java:109)
            at org.python.modules.zipimport.zipimporter.zipimporter_load_module(zipimporter.java:161)
            at org.python.modules.zipimport.zipimporter$zipimporter_load_module_exposer.__call__(Unknown Source)

    java.lang.OutOfMemoryError: java.lang.OutOfMemoryError: Java heap space


Start nxipython with the following arguments::

    $ java -Xms64m -Xmx256m -jar jython-nx-2.5.2.jar -mnxipython

