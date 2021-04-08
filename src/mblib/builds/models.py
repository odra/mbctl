from terminaltables import AsciiTable


class Build:
  _id = 0
  name = ''
  owner = ''
  rebuild_strategy = ''
  koji_tag  = ''
  status = ''
  reason = ''
  stream = ''

  def __init__(self, _id, name, owner, rebuild_strategy, koji_tag, status, reason, stream):
    self._id = _id
    self.name = name
    self.owner = owner
    self.rebuild_strategy = rebuild_strategy
    self.koji_tag = koji_tag
    self.status = status
    self.reason = reason
    self.stream = stream

  def __str__(self):
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


class BuildList:
  builds = []

  def __init__(self, *args):
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
    return [b.as_python() for b in self.builds]
