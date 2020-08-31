#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
del sys.path[0]

# Python 2 <=> 3 compat
if 2 < sys.version_info.major:
   readline = input     # Use new (Python 3+) input() method
else:
   readline = raw_input # Use old (Python 2.*) raw_input() method

