Change Log
==========

0.6 - unreleased
----------------

**Bug Fixes**
    - https://github.com/nexiles/nexiles.jython/issues/10: disable pip ssl cert
      checking on install due to no ssl in jython 2.5
    - https://github.com/nexiles/nexiles.jython/issues/8: pip and
      distribute versions are now automatically set when building.
    - https://github.com/nexiles/nexiles.jython/issues/9: pin virtualenv
      package -- they dropped python 2.5 support.

0.5 - 2013-02-14
----------------

**Improvements**
    - add new `wtshell` module -- use like `nxjython -mwtshell` for boxen
      where ipython does'nt work (Windows)
      https://github.com/nexiles/nexiles.jython/issues/1
    - now uses distribute instead of setuptools.  This means that we can
      now build binary eggs! Yay!
    - removed the python.org tests from the deployed package to save space.
    - the new fab task `install` which installs script wrappers
      https://github.com/nexiles/nexiles.jython/issues/3
    - Support for per-user `site-packages` :ref:`usage`

**Bug Fixes**
    - workaround for windows/ipython issue.
      https://github.com/nexiles/nexiles.jython/issues/1
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
