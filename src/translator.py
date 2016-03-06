import urllib
import re
from google.appengine.api import urlfetch

class Translator():
	def translate(self, text):
		url = 'http://tili.kg/dict/show-word/' + text
		result = urlfetch.fetch(url=url,
		    method=urlfetch.GET,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = []
		for i in re.finditer('<div class="gdarticle">([\w\W]+?)<\/div>', result.content):
			res.append(self.sanitize(i.group(1)))
		if res:
			return res
		return ['Котормосу жок']
	
	def sanitize(self, text):
		text = text.replace('<b>', '[b]')
		text = text.replace('</b>', '[/b]')
		text = re.sub("<span class='tip'>[\w\W]+?</span>", '', text)
		text = re.sub('<[\w\W]+?>', '', text)
		text = text.replace('&rarr;', '→')
		text = text.replace('[b]', '<b>')
		text = text.replace('[/b]', '</b>')
		return text