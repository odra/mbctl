import json

import pytest
import requests
import requests_mock

from mbctl import cli
from mblib import errors


@pytest.fixture
def expected():
  return {
    'mbctl': '0.1.0',
    'mbs': '3.4.1',
    'api': 2
  }


@pytest.fixture
def mocked():
  return {
    'version': '3.4.1',
    'api_version': 2
  }



def test_version_text(expected, mocked):
  with requests_mock.Mocker() as m:
    m.get('https://mbs.fedoraproject.org/module-build-service/1/about', text=json.dumps(mocked))
    actual = [chunk for chunk in cli.run(['version'])]
  
  assert [f'{k}: {v}' for k, v in expected.items()] == actual


def test_version_json(expected, mocked):
  with requests_mock.Mocker() as m:
    m.get('https://mbs.fedoraproject.org/module-build-service/1/about', text=json.dumps(mocked))
    actual = [chunk for chunk in cli.run(['version', '--output', 'json'])]
  
  assert expected == json.loads(actual[0])


def test_version_error():
  with requests_mock.Mocker() as m, pytest.raises(errors.MBError):
    m.get('https://mbs.fedoraproject.org/module-build-service/1/about', exc=requests.exceptions.ConnectTimeout)
    [chunk for chunk in cli.run(['version'])]
