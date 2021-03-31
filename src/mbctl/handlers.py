"""
This module contains CLI hanlders for each subcommand.
"""
import json

from mbctl import __version__
from mblib import httpclient


def version(output='text'):
  """
  Shows the CLI version
  """
  c = httpclient.Client('https://mbs.fedoraproject.org/module-build-service/1')
  code, data = c.request('/about')
  parsed = json.loads(data)
  if output == 'text':
    yield f'mbctl : {__version__}'
    yield f'module-build-service: {parsed["version"]}'
    yield f'api-version: {parsed["api_version"]}'
  else:
    yield json.dumps({
      'mbctl': __version__,
      'module-build-service': parsed['version'],
      'api-version': parsed['api_version']
    }, indent=4, sort_keys=True)

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
