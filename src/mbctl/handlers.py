"""
This module contains CLI hanlders for each subcommand.
"""
import json

from mbctl import __version__
from mblib import httpclient, parser
from mblib import version as version_lib
from mblib import build as build_lib


def version(output='text', **kwargs):
  """
  Shows the CLI version
  """
  c = httpclient.Client(kwargs['server_url'])
  code, data = c.request('/about')
  parsed = json.loads(data)
  model = version_lib.models.Version(__version__, parsed['version'], parsed['api_version'])
  
  return parser.parse(model, output=output)

def list(output='text', **kwargs):
  """
  lists builds based on filtered data
  """
  c = httpclient.Client(kwargs['server_url'])
  code, data = c.request('/module-builds')
  parsed = json.loads(data)
  model = build_lib.models.BuildList(*parsed['items'])
  output = output
  if output == 'text':
    output = 'table'
  return parser.parse(model, output=output)

def build():
  """
  Imports/triggers a build in MBS.
  """
  pass
