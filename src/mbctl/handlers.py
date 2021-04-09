"""
This module contains CLI hanlders for each subcommand.
"""
import json

from mbctl import __version__
from mblib import httpclient, parser, scm
from mblib import version as version_lib
from mblib import builds as build_lib


def version(output='text', ssl_verify=True, **kwargs):
  """
  Shows the CLI version
  """
  c = httpclient.Client(kwargs['server_url'], ssl_verify=ssl_verify)
  code, data = c.request('/about')
  parsed = json.loads(data)
  model = version_lib.models.Version(__version__, parsed['version'], parsed['api_version'])
  
  return parser.parse(model, output=output)

def list(output='text', ssl_verify=True, **kwargs):
  """
  lists builds based on filtered data
  """
  c = httpclient.Client(kwargs['server_url'], ssl_verify=ssl_verify)
  code, data = c.request('/module-builds/')
  parsed = json.loads(data)
  model = build_lib.models.BuildList(*parsed['items'])
  
  return parser.parse(model, output=output)


def build(output='text', ssl_verify=True, **kwargs):
  """
  Imports/triggers a build in MBS.
  """
  commit = kwargs['commit']
  repository = kwargs['repository']
  branch = kwargs['branch']
  if not commit:
    commit = scm.get_latest_commit(repository, branch)
  c = httpclient.Client(kwargs['server_url'], auth=httpclient.KRBAuth(), ssl_verify=ssl_verify)
  data = {
    'scmurl': f'{kwargs["repository"]}?#{commit}',
    'branch': kwargs['branch']
  }
  code, data = c.request('/module-builds', method='POST', data=json.dumps(data))
  if code != 201:
    raise errors.MBError(data)
  yield data
