#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

#cpu.load()
cpu.load_management("examples/stack.ls8")
cpu.run()
