from django_case_insensitive_field import CaseInsensitiveFieldMixin
from django.db import models

class UsernameField(CaseInsensitiveFieldMixin, models.CharField):
    
    def __init__(self, *args, **kwargs):

        super(CaseInsensitiveFieldMixin, self).__init__(*args, **kwargs) 