import sys
import os

import argparse


def parse_command_line_arguments():
    '''Parses the command line arguments and returns them.'''

    top_parser = argparse.ArgumentParser(
        prog='Block Diagrammer (BD)',
        description='''Creates block diagrams from simple text descriptions.'''
    )

    subparsers = top_parser.add_subparsers()

    build_render_subparser(subparsers)

    oArgs = top_parser.parse_args()

    print_help_if_no_command_line_options_given(top_parser)

    return oArgs


def build_render_subparser(oSubParser):

    parser = oSubParser.add_parser('render', help='Render input file into image')

    parser.add_argument('renderer', action='store', default=None, choices=['text', 'svg'], help='Selects render engine')
    parser.add_argument('file', action='store', metavar='FILENAME', default=None, help='File to render')

    parser.set_defaults(which='render')


def print_help_if_no_command_line_options_given(oParser):
    '''
    Will print the help output if no command line arguments were given.
    '''
    if len(sys.argv) == 1:
        oParser.print_help()
        sys.exit(1)
