"""
Error module.

All error classes should be declared in this module.
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

    Paramaters
    ----------
    message: str
      The error message

    code: int (defaults 1)
      The error code

    data: Any (defaults None)
      Additional error data, if any.

    Returns
    -------
    mblib.errors.MBError
      The error object instance
    """
    super(MBError, self).__init__(message)
    self.message = message
    self.code = code
    self.data = data

  def __str__(self):
    """
    Invoked by `str()` or `print()`

    Returns
    -------
    str
      A uer friendly string representation of the error.
    """
    return f'[{self.code}] {self.message}'

  def __repr__(self):
    """
    Invoked by `repr()`

    Returns
    -------
    str
      The non-user error string representation of the error.
    """
    name = self.__class__.__name__
    return f'{name}(\'{self.message}\', code={self.code}, data={self.data})'
