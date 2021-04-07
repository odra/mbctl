class Build:
  _id = ''
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

  def data(self):
    return [
      ('id', self._id),
      ('name', self.name),
      ('owner', self.owner),
      ('rebuild_strategy', self.rebuild_strategy),
      ('koji_tag', self.koji_tag),
      ('status', self.status),
      ('reason', self.reason),
      ('stream', self.stream)
    ]


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

  def keys(self):
    return ['ID', 'Name', 'Owner', 'Strategy', 'Koji Tag', 'Status', 'Reason','Stream']

  def values(self):
    data = []
    for build in self.builds:
      data.append([s[1] for s in build.data()])

    return data

  def data(self):
    return [
      ('builds', [{k: v for k,v in b.data()} for b in self.builds])
    ]
