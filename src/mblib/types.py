from abc import ABC, abstractmethod


class Model(ABC):
  """
  Abstract class for models.
  """

  @abstractmethod
  def __str__(self):
    """
    Return the string implementation of the object, used by str().

    Returns
    -------
    str
      The string reprensentation of the object instance.
    """
    raise NotImplemented

  @abstractmethod
  def as_python(self):
    """
    Return the dict version of the object.

    Returns
    -------
    dict
      The dict reprensentation of a theobject instance.
    """
    raise NotImplemented