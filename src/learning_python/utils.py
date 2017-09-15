import random
import string
import datetime
import math
import re

from django.conf import settings
from django.utils.text import slugify
from django.utils.html import strip_tags

from itsdangerous import URLSafeTimedSerializer

from rest_framework.views import exception_handler

def unique_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def create_slug(instance, new_slug=None):
	if not new_slug:
		slug = slugify(instance.title)
	else:
		slug = new_slug

	Klass = instance.__class__
	qs = Klass.objects.filter(slug=slug).order_by("-id")
	if qs.exists():
		string_unique = unique_string_generator()
		newly_created_slug = slug + "-{id}".format(id=string_unique)
		return create_slug(instance, new_slug=newly_created_slug)
	return slug

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt=settings.SECURITY_PASSWORD_SALT)

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=settings.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email

def count_words(html_string):
    # html_string = """
    # <h1>This is a title</h1>
    # """
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words) #joincfe.com/projects/
    return count

def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0) #assuming 200wpm reading
    # read_time_sec = read_time_min * 60
    # read_time = str(datetime.timedelta(seconds=read_time_sec))
    # read_time = str(datetime.timedelta(minutes=read_time_min))
    return int(read_time_min)

def customer_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        # if response.status_code == 400:
            # response.data['detail'] = "You were hacked"

        # if response.status_code == 401:
            # response.data['detail'] = "You were hacked"

        # if response.status_code == 404:
            # response.data['detail'] = "You were hacked"

        # if response.status_code == 405:
            # response.data['detail'] = "Error 405"
    
    return response