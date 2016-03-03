import urllib
import re
from google.appengine.api import urlfetch

class Translator():
	def translate(self, text):
		url = 'http://tili.kg/dict/show-word/' + text
		result = urlfetch.fetch(url=url,
		    method=urlfetch.GET,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = re.search('<div class="gdarticle">([\w\W]+?)<\/div>', result.content)
		if res:
			return re.sub('<[\w\W]+?>', '', res.group(1))
		return 'No translation'