"""
HTTP client module.
"""
import requests
from requests.auth import HTTPBasicAuth
from requests_kerberos import HTTPKerberosAuth

from . import errors


class KRBAuth:
  """
  Kerberos authenticaton type.
  """
  principal = None
  hostname_override = None

  def __init__(self, principal=None, hostname_override=None):
    self.principal = principal
    self.hostname_override = hostname_override

  def auth(self):
    params = {}
    if self.principal:
      params['principal'] = self.principal
    if self.hostname_override:
      params['hostname_override'] = self.hostname_override

    return HTTPKerberosAuth(**params)


class BasicAuth:
  username = ''
  password = ''

  def __init__(self, usernae, password):
    self.username = username
    self.password = password

  def auth(self):
    return HTTPBasicAuth(self.username, self.password)


class NoAuth:
  """
  No authentication type.
  """
  def auth(self):
    """
    This method does nothing, just a place holder for the
    "authentication interface".
    """
    return None


class Client:
  """
  A simple HTTP client to be used within the CLI code.
  """

  base_url = None
  auth = None

  def __init__(self, base_url, auth=NoAuth()):
    """
    Initializes the object with a base url and authentication type.

    Auth type can be 'basic' or 'krb' and defaults to None
    if no value is provided.
    """
    self.auth = auth
    if base_url:
      self.base_url = base_url

  def request(self, path, method='GET', data=None, headers=None):
    """
    Execute a request based on method parameters.

    Return a tuple containing the status_code and text output.
    """
    url = f'{self.base_url}{path}'
    try:
      res = requests.request(method, url, data=data, headers=headers, auth=self.auth.auth())
    except requests.exceptions.RequestException as e:
      raise errors.MBError(str(e))

    return (res.status_code, res.text)
