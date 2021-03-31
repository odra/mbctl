"""
CLI module to be used by mbctl script.

The `main` exists for sole purpose to be used by the 'mbctl' exectuable.
"""
import sys
import argparse

from . import handlers
from mblib import errors



output_parser = argparse.ArgumentParser(add_help=False)
output_parser.add_argument('--output', '-o', type=str, choices=['text', 'json'], default='text')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='MBS Client CLI')
# version subcommand
parser_version = subparsers.add_parser('version', help='shows CLI version', parents=[output_parser])
parser_version.set_defaults(_handler=handlers.version)
# list
parser_list = subparsers.add_parser('list', help='lists module filters')
parser_list.add_argument('--state', '-s', type=str, help='filter by build state', default='')
parser_list.add_argument('--id', type=str, help='filter by build id', default='')
parser_list.set_defaults(_handler=handlers.list)
# build
parser_build = subparsers.add_parser('build', help='builds a mobule')
parser_build.add_argument('repository', type=str, help='repository http url')
parser_build.add_argument('--branch', '-b', type=str, help='repository branch to use, defaults to rawhide', default='rawhide')
parser_build.add_argument('--commit', '-c', type=str, help='commit to use, will latest commit if not provided', default='')
parser_build.set_defaults(_handler=handlers.build)


def run(*args, **kwargs):
  """
  Parse the CLI arguments and run the subcommand specified handler.
  """
  ns = parser.parse_args(*args, **kwargs)
  try:
    params = {k:v for k,v in vars(ns).items() if k != '_handler'}
    for line in ns._handler(**params):
      yield line
  except AttributeError:
    raise errors.MBError('Invalid CLI usage')


def main(*args, **kwargs):
  """
  Main function to be used by a script.
  """
  try:
    for line in run(*args, **kwargs):
      print(line)
    sys.exit(0)
  except errors.MBError as e:
    sys.stderr.write(f'{e}\n')
    sys.exit(1)
