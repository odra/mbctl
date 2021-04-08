import hashlib
from types import SimpleNamespace as NS

import pytest

from mblib import scm


@pytest.fixture
def expected_sha1():
  return hashlib.sha1().hexdigest()


def test_get_latest_commit_ok(expected_sha1, mocker):
  mocker.patch('git.Repo.clone_from', return_value=NS(rev_parse=lambda refs: hashlib.sha1().hexdigest()))
  sha1 = scm.get_latest_commit('something.git', 'rawhide')

  assert expected_sha1 == sha1
