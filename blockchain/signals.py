from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . import models
from contract.models import ContractModel, DepositorModel, TrusteeModel, UserModel
from . import custom_signals


def get_all_related_email(contract):

    depositors_email = []

    owner: UserModel = contract.owner

    try:

        depositors_email: list = list(
            contract.depositors.all().values_list('user__email', flat=True))

    except DepositorModel.DoesNotExist:

        pass

    trustees_email: list = []

    try:

        trustees_email: list = list(
            contract.trustees.all().values_list('user__email', flat=True))

    except TrusteeModel.DoesNotExist:

        pass

    emails = trustees_email + depositors_email

    emails.append(owner.email)

    return set(emails)


def emailer(instance: models.TransactionModel, template: str, title: str):

    # send an e-mail to the user on deposit/request for withdrawal

    contract: ContractModel = instance.contract

    context = {
        'transaction_hash': instance.transaction_hash,
        'identifier': instance.identifier,
        'contract_id': contract.id,
        'amount': instance.amount,
        'block_hash': instance.transaction_hash,
        'creator': instance.creator,
        'description': instance.description,
        'type': instance.type,
        'status': instance.status,
        'token_symbol': contract.token.symbol,
    }

    emails = get_all_related_email()

    # render email text
    email_html_message = render_to_string(
        f'blockchain/{template}/index.html', context)
    email_plaintext_message = render_to_string(
        f'blockchain/{template}/index.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        title,
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_SENDER,
        # to:
        set(emails)
    )

    msg.attach_alternative(email_html_message, "text/html")

    msg.send()


@receiver(post_save, sender=models.TransactionModel)
def email_on_new_transaction(sender, instance: models.TransactionModel, created, *args, **kwargs):

    # send an e-mail to the user on deposit/request for withdrawal

    if created and instance.transaction_hash:

        emailer(instance, 'deposit',
                f"A new transaction occurred in your contract #{instance.contract.id}")
        
    elif created:

        emailer(instance, 'request',
                f"A new transaction occurred in your contract #{instance.contract.id}")
        
    


@receiver(custom_signals.reject_withdrawal, sender=models.TrusteeModel)
def email_reject_to_client(sender, instance, *args, **kwargs):

    emailer(instance, 'reject',
            f"A new transaction occurred in your contract #{instance.contract.id}")


@receiver(custom_signals.reject_withdrawal, sender=models.TrusteeModel)
def email_withdrawal_to_client(sender, instance, *args, **kwargs):

    emailer(instance, 'withdrawal',
            f"A new transaction occurred in your contract #{instance.contract.id}")


@receiver(custom_signals.reject_withdrawal, sender=models.TrusteeModel)
def email_withdrawal_approval_to_client(sender, instance, *args, **kwargs):

    emailer(instance, 'approval',
            f"A new transaction occurred in your contract #{instance.contract.id}")
