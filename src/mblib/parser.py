"""
Parser module.
"""
import json

from terminaltables import AsciiTable


def parse(model, output='text'):
  """
  Parses a model into other data, possible values are "text" or "json".

  Parameters
  ----------
  model: mblib.types.Model
    A mblib model implementation

  output: str (default "text")
    The output type to parse to, valid choices: text, json 
  """
  if output == 'json':
    return as_json(model)
  return as_text(model)


def as_text(model):
  """
  Parses a model into a raw text string.

  Paramaters
  ----------
  model: mblib.types.Model
    A mblib model implementation

  Returns
  -------
  str
    The string representation of the model invoked by __str__.
  """
  return str(model)


def as_json(model):
  """
  Parses a model into a json string.

  It should work as long as `model.as_python()` returns
  an object that can be dumped to a json string.

  Paramaters
  ----------
  model: mblib.types.Model
    A mblib model implementation

  Returns
  -------
  str
    A json string representation of the model.
  """
  return json.dumps(model.as_python(), indent=4, sort_keys=True)
