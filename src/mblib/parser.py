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
  """
  for k, v in model.data():
    yield f'{k}: {v}'


def parse_json(model):
  """
  Parses a model into a json string.
  """
  data = {}
  for k, v in model.data():
    data[k] = v
  yield json.dumps(data, indent=4, sort_keys=True)


def parse_table(model):
  """
  Parse model as table.
  """
  data = [model.keys()] + model.values()
  table = AsciiTable(data)
  for line in table.table.split('\n'):
    yield line
