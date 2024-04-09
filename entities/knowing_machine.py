# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from yaml import load, FullLoader
from json import dumps


knom = """
name: knowing_machine
description: Knows everything you ask it about and answers your question. Please be concise with your question, but provide enough context.
input_schema:
  type: object
  properties:
    question:
      type: string
      description: The question to be answered.
    context:
      type: string
      description: The context to be used for answering the question.
required:
  - question
"""

KNOWING_MACHINE = load(knom, Loader=FullLoader)

# print(KNOWING_MACHINE)