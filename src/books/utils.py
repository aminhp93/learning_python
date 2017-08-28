from rest_framework.views import exception_handler

def customer_exception_handler(exc, context):
	response = exception_handler(exc, context)

	if response is not None:
		response.data['status_code'] = response.status_code
		if response.status_code == 401:
			response.data['detail'] = "You were hacked"

	
	return response