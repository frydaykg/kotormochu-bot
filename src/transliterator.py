import urllib
import re
from google.appengine.api import urlfetch
import logging
import json

class Transliterator():
  def transliterate(self, text):
    m = get_map()
    for key in m:
      text = text.replace(key, m[key])
    return text

  def get_map():
    d = {
    '-о-': u'ө',
    '-у-': u'ү',
    '-н-': u'ң',
    '-О-': u'Ө',
    '-У-': u'Ү',
    '-Н-': u'Ң',
    }
    return d
