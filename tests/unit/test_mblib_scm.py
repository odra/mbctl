import hashlib
from types import SimpleNamespace as NS

import pytest

from mblib import scm, errors


def _sha1():
  return hashlib.sha1().hexdigest()


@pytest.fixture
def expected_sha1():
  return _sha1()


def test_get_latest_commit_ok(expected_sha1, mocker):
  mocker.patch('git.Repo.clone_from', return_value=NS(rev_parse=lambda refs: _sha1()))
  sha1 = scm.get_latest_commit('something.git', 'rawhide')

  assert expected_sha1 == sha1


def test_get_latest_commit_error(expected_sha1, mocker):
  with pytest.raises(errors.MBError):
    sha1 = scm.get_latest_commit('something.git', 'rawhide')
