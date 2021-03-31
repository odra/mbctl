import pytest

from mblib import errors


def err(msg, **kwargs):
  return errors.MBError(msg, **kwargs)


@pytest.mark.parametrize(
  'expected,current', [
    ('[1] pytest.fixture.error', err('pytest.fixture.error')),
    ('[5] pytest.fixture.error_code', err('pytest.fixture.error_code', code=5))
  ]
)
def test_str(expected, current):
  assert expected == str(current)


@pytest.mark.parametrize(
  'expected,current', [
    ('MBError(\'pytest.fixture.error\', code=1, data=None)', err('pytest.fixture.error')),
    ('MBError(\'pytest.fixture.error\', code=2, data={\'foo\': \'bar\'})', err('pytest.fixture.error', code=2, data={'foo': 'bar'})),
  ]
)
def test_repr(expected, current):
  assert expected == repr(current)
