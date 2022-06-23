from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . import models
import logging

logger = logging.getLogger('django')


@receiver(post_save, sender=models.DepositorModel)
def email_payment_request_to_depositor(sender, instance: models.DepositorModel, created, *args, **kwargs):

    if created:
    
        # send an e-mail to the user

        user: models.UserModel = instance.user
        
        contract : models.ContractModel = instance.contract
        
        token : models.TokenModel = contract.token
        
        email = user.email
        
        contract_owner_email = contract.owner.email
        
        context = {
            'title': contract.title,
            'email': email,
            'amount': instance.amount,
            'wallet_address' : instance.wallet_address,
            'contract_id': contract.id,
            'contract_owner_email' : contract_owner_email,
            'token_symbol': token.symbol,
            'token_network_name': token.network.name,
        }

        # render email text
        email_html_message = render_to_string(
            'contract/depositor/index.html', context)
        email_plaintext_message = render_to_string(
            'contract/depositor/index.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            f"{email} added you to contract #{contract.id}",
            # message:
            email_plaintext_message,
            # from:
            settings.EMAIL_SENDER,
            # to:
            [user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()
        
        
@receiver(post_save, sender=models.TrusteeModel)
def email_payment_request_to_trustee(sender, instance, created, *args, **kwargs):
    
    if created:
        
        # send an e-mail to the user

        user: models.UserModel = instance.user
        
        contract : models.ContractModel = instance.contract
        
        token : models.TokenModel = contract.token
        
        email = user.email
        
        contract_owner_email = contract.owner.email
        
        context = {
            'title': contract.title,
            'email': email,
            'amount': instance.amount,
            'wallet_address' : instance.wallet_address,
            'contract_id': contract.id,
            'contract_owner_email' : contract_owner_email,
            'token_symbol': token.symbol,
            'token_network': token.network,
        }

        # render email text
        email_html_message = render_to_string(
            'contract/trustee/index.html', context)
        email_plaintext_message = render_to_string(
            'contract/trustee/index.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            f"{email} added you to contract #{contract.id}",
            # message:
            email_plaintext_message,
            # from:
            settings.EMAIL_SENDER,
            # to:
            [user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()