Change Log
==========

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
