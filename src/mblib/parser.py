"""
Parser module.
"""
import json

from terminaltables import AsciiTable


def parse(model, output='text'):
  """
  Parses a model into other data, possible values are "text" or "json".

  Should return a generator with the parsed data.
  """
  if output == 'json':
    return parse_json(model)
  if output == 'table':
    return parse_table(model)
  return parse_text(model)


def parse_text(model):
  """
  Parses a model into a raw text string.

  The model needs to implement `__str__`.
  """
  return str(model)


def parse_json(model):
  """
  Parses a model into a json string.

  The model needs to implement a `to_python` method
  to return a object that can be dumped to json, such as a dict or list.
  """
  return json.dumps(model.as_python(), indent=4, sort_keys=True)
