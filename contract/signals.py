from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . import models
import logging

logger = logging.getLogger('django')
logger.error("user.email")

@receiver(post_save, sender=models.DepositorModel)
def email_payment_request_to_depositor(sender, instance, created, *args, **kwargs):
    
    logger.error(created)

    # if created:
    
    #     # send an e-mail to the user

    #     user: models.UserModel = instance.user

    #     context = {
    #         'username': user.username,
    #         'email': user.email,
    #         'amount': instance.amount,
    #         'wallet_address' : instance.wallet_address,
    #         'contract_id': instance.contract.id,
    #     }

    #     # render email text
    #     email_html_message = render_to_string(
    #         'contract/base.html', context)
    #     email_plaintext_message = render_to_string(
    #         'contract/base.txt', context)

    #     msg = EmailMultiAlternatives(
    #         # title:
    #         f"Someone added you as a Depositor",
    #         # message:
    #         email_plaintext_message,
    #         # from:
    #         settings.EMAIL_SENDER,
    #         # to:
    #         [user.email]
    #     )
    #     msg.attach_alternative(email_html_message, "text/html")
    #     msg.send()
        
        
# @receiver(post_save, sender=models.TrusteeModel)
# def email_payment_request_to_trustee(sender, instance, created, *args, **kwargs):
    
#     logger.error("user.email")
#     logger.error(created)

#     if created:
    
#         # send an e-mail to the user

#         user: models.UserModel = instance.user

#         context = {
#             'username': user.username,
#             'email': user.email,
#             'amount': instance.amount,
#             'wallet_address' : instance.wallet_address,
#             'contract_id': instance.contract.id,
#         }

#         # render email text
#         email_html_message = render_to_string(
#             'contract/base.html', context)
#         email_plaintext_message = render_to_string(
#             'contract/base.txt', context)

#         msg = EmailMultiAlternatives(
#             # title:
#             f"Someone Added you as a Trustee",
#             # message:
#             email_plaintext_message,
#             # from:
#             settings.EMAIL_SENDER,
#             # to:
#             [user.email]
#         )
#         msg.attach_alternative(email_html_message, "text/html")
#         msg.send()