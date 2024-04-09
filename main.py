# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from json import dumps
from entities.knowing_machine import KNOWING_MACHINE
from entities.memory_machine import MEMORY_MACHINE

if __name__ == "__main__":
    objects = [KNOWING_MACHINE, MEMORY_MACHINE]
    tools = dumps(objects)
    print(tools)