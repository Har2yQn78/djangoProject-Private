import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase


#  for additional documentation https://docs.python.org/3/library/unittest.html
class djangoProjectConfigTest(TestCase):
    def test_secret_key(self, do_something=None):
        SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-z=3clw@!=27s$^e%_zaw3jg2kp!qbv3$+2lbrp8l*hcl2(x4a6')

        try:
            is_strong = validate_password('django-insecure-z=3clw@!=27s$^e%_zaw3jg2kp!qbv3$+2lbrp8l*hcl2(x4a6')
        except Exception as e:
            msg = f'weak Secret_key'
            self.fail(msg)