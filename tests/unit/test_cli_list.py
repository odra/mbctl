from mbctl import cli


def test_cli_ok():
  cli.run(['list'])
