import json

import pytest

from mblib import parser, types


class Model(types.Model):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def as_python(self):
    return {'name': self.name}  


def test_parse_text():
  m = Model('foobar')
  assert 'foobar' == parser.parse(m, output='text')


def test_parse_as_json():
  m = Model('foobar')
  expected = {
    'name': 'foobar'
  }
  actual = parser.parse(m, output='json')

  assert expected == json.loads(actual)