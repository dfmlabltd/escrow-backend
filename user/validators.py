from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from re import match

# creating a validator function
def validate_username(username):
    
    
    if not match('^(?![0-9]+)', username):

        raise ValidationError(
            _('username must not start with a number'))

    if not match('^[a-zA-Z0-9]+$', username):

        raise ValidationError(
            _('username must contain only alphanumerical characters'))

    return username