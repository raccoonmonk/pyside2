#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of PySide2.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import sys
import unittest
from PySide2 import QtCore

class MyObject(QtCore.QObject):
    def __init__(self, other=None):
        QtCore.QObject.__init__(self, None)
        self._o = other

class TestDestructor(unittest.TestCase):
    def testReference(self):
        o = QtCore.QObject()
        m = MyObject(o)
        self.assertEqual(sys.getrefcount(o), 3)
        del m
        self.assertEqual(sys.getrefcount(o), 2)

if __name__ == '__main__':
    unittest.main()
