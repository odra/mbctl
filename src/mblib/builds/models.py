"""
This module has data classes for build related data. 
"""

from terminaltables import AsciiTable

from mblib import types


class Build(types.Model):
  """
  Build data class.
  """
  _id = 0
  name = ''
  owner = ''
  rebuild_strategy = ''
  koji_tag  = ''
  status = ''
  reason = ''
  stream = ''

  def __init__(self, _id, name, owner, rebuild_strategy, koji_tag, status, reason, stream):
    """
    Initializes a `Build` object.

    Parameters
    ----------
      _id: int
        Build ID
      name: str
        Build name
      owner: str
        Build owner
      rebuild_stratgy: str
        Build strategy
      koji_tag: str
        The koji tag for this build
      status: str
        The status name for this build, such as "ready"
      reason: str
        The build status reason which gives more context to the status name
      stream: str
        The build stream/branch
    Returns
    -------
      Build
        A Build object instance.
    """
    self._id = _id
    self.name = name
    self.owner = owner
    self.rebuild_strategy = rebuild_strategy
    self.koji_tag = koji_tag
    self.status = status
    self.reason = reason
    self.stream = stream

  def __str__(self):
    """
    Return the srting version of the object, used by __str__.

    Returns
    -------
    str
      The string reprensentation of a `Build` object instance.
    """
    return '\n'.join([
      f'ID: {self.id}',
      f'Name: {self.name}',
      f'Owner: {self.owner}',
      f'Rebuild Strategy: {self.rebuild_strategy}',
      f'Koji Tag: {self.koji_tag}',
      f'Status: {self.status}',
      f'Reason: {self.reason}',
      f'Stream: {self.stream}'
    ])

  def as_python(self):
    """
    Return the dict version of the object.

    Returns
    -------
    dict
      The dict reprensentation of a `Build` object instance.
    """
    return {
      'id': self._id,
      'name': self.name,
      'owner': self.owner,
      'rebuild_strategy': self.rebuild_strategy,
      'koji_tag': self.koji_tag,
      'status': self.status,
      'reason': self.reason,
      'stream': self.stream
    }


class BuildList(types.Model):
  """
  BuildList data class.

  This class serves the purpose to provide a container for a lisr
  of builds.
  """
  builds = []

  def __init__(self, *args):
    """
    Initializes a `BuildList` object.

    Parameters
    ----------
    *args: list[dict]
      A list of dicts that comes from mbs which each item will be serialized to a `Build` object.

    Returns
    -------
    BuildList
      A BuildList object instance.
    """
    for data in args:
      self.builds.append(
        Build(data['id'],
          data['name'],
          data['owner'],
          data['rebuild_strategy'],
          data['koji_tag'],
          data['state_name'],
          data['state_reason'],
          data['stream'])
      )

  def __str__(self):
    """
    Return the srting representation of the object, used by __str__.

    Returns
    -------
    str
      The string reprensentation of a `BuildList` object instance (table format).
    """
    output = []
    keys = ['ID', 'Name', 'Owner', 'Strategy', 'Koji Tag', 'Status', 'Reason','Stream']
    values = []
    
    for build in self.builds:
      values.append([
        build._id,
        build.name,
        build.owner,
        build.rebuild_strategy,
        build.koji_tag,
        build.status,
        build.reason,
        build.stream
      ])
    
    return AsciiTable([keys] + values).table

  def as_python(self):
    """
    Return a list of dicts for this object.

    Returns
    -------
    list[dict]
      The list of dicts reprensentation of a `BuildList` object instance.
    """
    return [b.as_python() for b in self.builds]
