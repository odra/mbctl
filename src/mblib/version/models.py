class Version:
  mbctl = None
  mbs = None
  api = None

  def __init__(self, mbctl, mbs, api):
    self.mbctl = mbctl
    self.mbs = mbs
    self.api = api

  def data(self):
    return [
      ('mbctl', self.mbctl),
      ('mbs', self.mbs),
      ('api', self.api)
    ]
