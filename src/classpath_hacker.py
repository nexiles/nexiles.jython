# -*- coding: utf-8 -*-
#
# File: .py
#
# Copyright (c) nexiles GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#import java.lang.reflect.Method
import java.lang.Object
from java.lang import ClassLoader
from java.io import File
from java.net import URL
from java.net import URLClassLoader
import jarray


class ClassPathHacker(object):
    """Original Author: SG Langer Jan 2007, conversion from Java to Jython
    Updated version (supports Jython 2.5.2) >From http://glasblog.1durch0.de/?p=846

    Purpose: Allow runtime additions of new Class/jars either from
    local files or URL
    """

    def __init__(self):
        self.system_class_loader = ClassLoader.getSystemClassLoader()
        self.url_class_loader = URLClassLoader

    def addFile(self, s):
        """Purpose: If adding a file/jar call this first
        with s = path_to_jar"""
        # make a URL out of 's'
        f = File(s)
        u = f.toURL()
        a = self.addURL(u)
        return a

    def addURL(self, u):
        """Purpose: Call this with u= URL for
         the new Class/jar to be loaded
        """
        method = self.url_class_loader.getDeclaredMethod("addURL", [URL])
        method.setAccessible(1)
        jarray.array([u], java.lang.Object)
        method.invoke(self.system_class_loader, [u])
        return u

# vim: set ft=python ts=4 sw=4 expandtab :
