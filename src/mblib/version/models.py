from mblib import types


class Version(types.Model):
  """
  Version data class.
  """
  mbctl = None
  mbs = None
  api = None

  def __init__(self, mbctl, mbs, api):
    """
    Initializes a `Version` object.

    Parameters
    ----------
      mbctl: str
        The mbctl cli version
      mbs: str
        The module-build-service instance version
      api: int
        The module-build-service api version 

    Returns
    -------
      Version
        A Version object instance.
    """
    self.mbctl = mbctl
    self.mbs = mbs
    self.api = api

  def __str__(self):
    """
    Return the srting version of the object used by __str__.

    Returns
    -------
    str
      The string reprensentation of a `Version` object instance.
    """
    return '\n'.join([
      f'mbctl: {self.mbctl}',
      f'mbs: {self.mbs}',
      f'api: {self.api}'
    ])

  def as_python(self):
    """
    Return the dict version of the object.

    Returns
    -------
    dict
      The dict reprensentation of a `Version` object instance.
    """
    return {
      'mbctl': self.mbctl,
      'mbs': self.mbs,
      'api': self.api
    }
