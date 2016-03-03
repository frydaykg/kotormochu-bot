from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import urllib
import re
from google.appengine.api import urlfetch
from api import Api
from translator import Translator

class Main(webapp.RequestHandler):
	def post(self):
		update = json.loads(self.request.body)
		if 'message' in update:
			message = update['message']
			if 'text' in message:
				text = text = message['text'].encode('utf-8')
				chat = message['chat']
				Api().send(chat['id'], Translator().translate(text), messageId = message['message_id'])

application = webapp.WSGIApplication([('/.*', Main)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
