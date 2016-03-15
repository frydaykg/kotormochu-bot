import urllib
import re
from google.appengine.api import urlfetch
import logging
import json

class Translator():
	def translate(self, text):
		url = 'http://tili.kg/dict/api/word/' + text
		result = urlfetch.fetch(url=url,
		    method=urlfetch.GET,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = []
		translations = json.loads(result.content)
		for i in translations:
			res.append(i['value'])
		if res:
			return res
		return ['Котормосу жок/Перевода нет']