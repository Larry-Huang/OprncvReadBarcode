#-----------------------------------------------------------------------------
# Copyright (c) 2015-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

import os
import sys

root = os.path.join(sys._MEIPASS, 'kivy_install')

os.environ['KIVY_DATA_DIR'] = os.path.join(root, 'data')
os.environ['KIVY_MODULES_DIR'] = os.path.join(root, 'modules')
