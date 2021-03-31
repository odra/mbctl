"""
This module contains CLI hanlders for each subcommand.
"""
from mbctl import __version__


def version():
  """
  Shows the CLI version
  """
  yield __version__

def list():
  """
  lists builds based on filtered data
  """
  pass


def build():
  """
  Imports/triggers a build in MBS.
  """
  pass
