#!/usr/bin/env python

import sys
import os
import yaml

from . import cmd_line_args
from . import subcommand
from . import utils


subCommandMap = {}
subCommandMap['render'] = subcommand.render.execute


def main():
    '''Main routine of the Block Diagrammer program.'''

    options = cmd_line_args.parse_command_line_arguments()
    options.fileDict = utils.read_yaml_file(options.file)

    subCommandMap[options.which](options)
