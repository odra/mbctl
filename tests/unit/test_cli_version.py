from mbctl import cli


def test_version():
  res = [chunk for chunk in cli.run(['version'])]
  assert ['0.1.0'] == res
