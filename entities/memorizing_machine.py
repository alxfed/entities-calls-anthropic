# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from util import githubf as ghf
from yaml import load, FullLoader


if getenv("GITHUB_TOKEN") is not None:
    organization = 'memorizing-machine'
    repo = 'memorizing-machine-private'
    file = 'machine.yaml'
    repo = ghf.creupdate_repo(organization=organization,
                              repository_name=repo,
                              private=True)
    memm = ghf.read_file(repository=repo,
                         file_path=file)
else:
    memm = """
name: memorizing_machine
description: Memorizes everything you ask it to remember and recalls it later, if you ask it to.
input_schema:
  type: object
  properties:
    memorize:
      type: string
      description: The thing to be remembered. This parameter should be used if you need to memorize something that will be necessary later. Dn not use this parameter if you are trying to recall something that you have memorized.
    context:
      type: string
      description: Why it should be remembered.
    recall:
      type: string
      description: The description of the thing to be recalled. This parameter should only be used if you need to recall something that you have memorized. Do not use this parameter if you are trying to memorize something.
"""
MEMORIZING_MACHINE = load(memm, Loader=FullLoader)


if __name__ == "__main__":
    print(MEMORIZING_MACHINE)