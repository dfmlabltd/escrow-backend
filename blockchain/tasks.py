from . import models
from celery import shared_task
from . import enums


@shared_task
def deposit(identifier, contract_address, trustee, amount, transaction_hash, block_hash):

    contract = models.ContractModel.objects.get(
        contract_address=contract_address)

    models.TransactionModel.objects.get_or_create(identifier=identifier,
                                                  type=enums.TransactionType.DEPOSIT.value,
                                                  contract=contract, defaults={
                                                      "transaction_hash": transaction_hash, "block_hash": block_hash,
                                                      "amount": amount, "creator": trustee,
                                                      "status": enums.TransactionType.DEPOSIT.value,
                                                  })


@shared_task
def request_for_withdrawal(identifier, contract_address, depositor, amount, description, transaction_hash, block_hash):

    contract = models.ContractModel.objects.get(
        contract_address=contract_address)

    models.TransactionModel.objects.get_or_create(identifier=identifier, type=enums.TransactionType.WITHDRAWAL.value,
                                                  contract=contract, defaults={
                                                      "amount": amount,
                                                      "transaction_hash": transaction_hash, "block_hash": block_hash,
                                                      "amount": amount, "creator": depositor, "description": description,
                                                  })


@shared_task
def reject_withdrawal(identifier, contract_address):

    contract = models.ContractModel.objects.get(identifier=identifier,
                                                contract_address=contract_address,
                                                type=enums.TransactionType.WITHDRAWAL.value)

    contract.status = enums.TransactionStatus.REJECTED.value

    contract.save()


@shared_task
def approve_withdrawal(identifier, contract_address):

    contract = models.ContractModel.objects.get(identifier=identifier,
                                                contract_address=contract_address,
                                                type=enums.TransactionType.WITHDRAWAL.value)

    contract.status = enums.TransactionStatus.ACCEPTED.value

    contract.save()



@shared_task
def withdrawal(identifier, contract_address):

    contract = models.ContractModel.objects.get(identifier=identifier,
                                                contract_address=contract_address,
                                                type=enums.TransactionType.WITHDRAWAL.value)

    contract.status = enums.TransactionStatus.COMPLETED.value

    contract.save()
