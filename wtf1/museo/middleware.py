import requests
from django.conf import settings
import webbrowser

class StackOverflowMiddleware(object):

	def __init__(self,get_response):
		self.get_response=get_response

	def __call__(self,request):
		return self.get_response(request)

	def process_exception(self,request,exception):
		intitle=u'{}:{}'.format(exception.__class__.__name__,str(exception))
		print(intitle,'Thats elemementary')
		webbrowser.open_new("https://www.google.co.in/search?q="+str(exception))
		return None