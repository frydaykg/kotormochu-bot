import urllib
import re
from google.appengine.api import urlfetch
import logging
import json

class Transliterator():
  def transliterate(self, text):
    m = self.get_map()
    for key in m:
      text = text.replace(key, m[key])
    return text

  def get_map(self):
    d = {
    '-о-': 'ө',
    '-у-': 'ү',
    '-н-': 'ң',
    '-О-': 'Ө',
    '-У-': 'Ү',
    '-Н-': 'Ң',
    }
    return d
