
from datetime import datetime

from . import views


class trial1(object):
    def process_request(self, request):
        request._request_time = datetime.now()

    def process_template_response(self, request, response):
        
    	if views.createpost.gtime == 1:

	        response_time = request._request_time - datetime.now()
	        response.context_data['response_time'] = abs(response_time)
	        return response