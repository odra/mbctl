"""
HTTP client module.
"""
import requests
from requests.auth import HTTPBasicAuth
from requests_kerberos import HTTPKerberosAuth

from . import errors, types


class KRBAuth(types.HttpAuth):
  """
  Kerberos authenticaton type.
  """
  principal = None
  hostname_override = None

  def __init__(self, principal=None, hostname_override=None):
    """
    Initialized the KRBAuth class

    Parameters
    ----------
    principal: str
      The kerberos principal to use instead of the default one

    hostname_override: str
      The kerberos hostname to use instead of the defult one
    """
    self.principal = principal
    self.hostname_override = hostname_override

  def auth(self):
    """
    Authenticates the request using kerberos.

    Returns
    -------
    request_kerberos.HTTPKerberosAuth
      A kerberos request object to be used by the requests library
    """
    params = {}
    if self.principal:
      params['principal'] = self.principal
    if self.hostname_override:
      params['hostname_override'] = self.hostname_override

    return HTTPKerberosAuth(**params)


class BasicAuth(types.HttpAuth):
  """
  Basic HTTP auth class.
  """
  username = ''
  password = ''

  def __init__(self, username, password):
    """
    Initializes the class by setting some properties.

    Parameters
    ----------
    username: str
      The request username to use

    password: str
      the request password to use

    Returns
    -------
    mblib.httpclient.BasicAuth
      A BasicAuth instance   
    """
    self.username = username
    self.password = password

  def auth(self):
    """
    Authenticates the request using kerberos.

    Returns
    -------
    requests.auth.HTTPBasicAuth
      A basic requests object to be used by the requests library
    """
    return HTTPBasicAuth(self.username, self.password)


class NoAuth(types.HttpAuth):
  """
  No authentication type.

  This class does no authentication at all.
  """
  def auth(self):
    """
    This method does nothing.

    Returns
    -------
    None
      It doesn't return anything
    """
    return None


class Client:
  """
  A simple HTTP client to be used within the CLI code.
  """

  base_url = None
  auth = None
  ssl_verify = True

  def __init__(self, base_url, auth=NoAuth(), ssl_verify=True):
    """
    Initializes the object with a base url and authentication type.

    Auth type can be 'basic' or 'krb' and defaults to None
    if no value is provided.

    Parameters
    ----------
    base_url: str
      The request base url to be used when doing requests.

    auth: mblib.types.HttpAuth
      An implemention of the HttpAuth abstract class

    Returns
    -------
    mblib.httpclient.CLient
      A instance of the Client class
    """
    assert issubclass(auth.__class__, types.HttpAuth)

    self.auth = auth
    self.base_url = base_url
    self.ssl_verify = ssl_verify

  def request(self, path, method='GET', data=None, headers=None):
    """
    Executes a http request based on method parameters.

    Parameters
    ----------
    path: str
      The path to make the request to
    
    method: str (defaults "GET")
      The HTTP method to use
    
    data: str (defaults None)
      Optional data to be sent in the request body
    
    headers: dict
      Additional headers to be set in the request

    Returns
    -------
    tuple
      A tuple contaning two items: http response code and the raw request response (str)
    """
    url = f'{self.base_url}{path}'
    try:
      res = requests.request(method, url, data=data, headers=headers, auth=self.auth.auth(), verify=self.ssl_verify)
    except requests.exceptions.RequestException as e:
      raise errors.MBError(str(e))

    return (res.status_code, res.text)
