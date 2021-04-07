"""
Error module.
"""

class MBError(Exception):
  """
  Base project exception, specelized exceptions should inherit from this
  class if one is needed.
  """
  code = 1
  msg = ''
  data = None

  def __init__(self, message, code=1, data=None):
    """
    Creates a new exception instance.
    """
    super(MBError, self).__init__(message)
    self.message = message
    self.code = code
    self.data = data

  def __str__(self):
    """
    Return a user friendly string reprensentation of the error.
    """
    return f'[{self.code}] {self.message}'

  def __repr__(self):
    """
    Return a "debug oriented" string representation of the error.
    """
    name = self.__class__.__name__
    return f'{name}(\'{self.message}\', code={self.code}, data={self.data})'
