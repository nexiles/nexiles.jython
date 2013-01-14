Change Log
==========

0.5 - unreleased
----------------

**Improvements**
    - removed the python.org tests from the deployed package to save space.
    - the new fab task `install` which installs script wrappers
      https://github.com/nexiles/nexiles.jython/issues/3

**Bug Fixes**
    - Fix a bug where distutils would break.
      https://github.com/nexiles/nexiles.jython/issues/5

0.4 - 2013-01-01
----------------

**Improvements**
    - Improved the docs.
      https://github.com/nexiles/nexiles.jython/issues/2

    - added `LICENSE.txt`

0.3 - 2013-01-10
----------------

**Improvements**
    - We now add WEB-INF/lib-python to the path using site.addsitedir().
      This is symmetric to how modjy initializes the python interpreter and
      will also process pth files.  This is only done when WT_HOME is set."

0.2 - 2013-01-07
----------------

**Packages**
    - reverted to flask 0.8 -- the 0.9 version is no longer python 2.5
      compatible.

**Jython Tools**
    - Added the `classpath_hacker` module.  This allows to dynamically add
      jar files to the currently running JVM
    - Added a workaround for #1 -- on windows, a plain jython repl is
      started instead the ipython one.
    - Added `monkey` module containing some monkey pathches we found to be
      needed.

0.1 - 2013-01-04
----------------

**Build System**
    - distribution fab task
    - fixed clean task

**Documentation**
    - added introduction section
    - added usage section
    - added changelog

..  vim: set ft=rst tw=75 nocin nosi ai sw=4 ts=4 expandtab:
