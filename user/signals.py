from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . import models



@receiver(post_save, sender=models.OTPModel)
def email_auth_otp_to_user(sender, instance, created, *args, **kwargs):

    if created:
    
        # send an e-mail to the user

        user: models.PasswordlessUserModel = instance.user

        context = {
            'username': user.username,
            'email': user.email,
            'code': instance.code,
        }

        # render email text
        email_html_message = render_to_string(
            'user/login/index.html', context)
        email_plaintext_message = render_to_string(
            'user/login/index.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            f"Passwordless Authentication Code",
            # message:
            email_plaintext_message,
            # from:
            settings.EMAIL_SENDER,
            # to:
            [user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()