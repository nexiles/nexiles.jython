==============
Monkey Patches
==============

Abstract
========

This version of jython includes several monkey patches we found
to be needed.

List of Patches applied
=======================

**Missing SOL_TCP constant in socket**
    The `socket` module misses the `SOL_TCP` constant.  This patch fises it.

**Missing 'idna' encoding**
    This is a gross hack which installs the `utf8` codec as mock `idna`
    codec.  YMMMV.

**Add default mimetype for JSON**
    Another hack which adds a default mime type for JSON.

