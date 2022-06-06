from rest_framework import permissions
from django.db.models import QuerySet
from . import models


def is_depositor(obj: models.DepositorModel.DoesNotExist, user: models.UserModel):

    try:

        depositors: QuerySet = obj.depositors.all()

        depositors.get(user=user)

        return True

    except models.DepositorModel.DoesNotExist:

        return False


def is_trustee(obj: models.TrusteeModel.DoesNotExist, user: models.UserModel):

    try:

        trustees: QuerySet = obj.trustees.all()

        trustees.get(user=user)

        return True

    except models.TrusteeModel.DoesNotExist:

        return False


class ContractReadOnlyPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_object_permission(self, request, view, obj):
        
        if request.method != 'GET':
            
            return True

        current_user: models.UserModel = request.user

        return obj.owner or is_trustee(obj, current_user) or is_depositor(obj, current_user)
