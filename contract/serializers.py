from rest_framework import serializers
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from typing import List, Dict
from django.utils.translation import ugettext_lazy as _


class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            obj, _ = queryset.get_or_create(**{self.slug_field: data})
            return obj
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field,
                      value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, obj):
        return getattr(obj, self.slug_field)


class EntitySerializer(serializers.ModelSerializer):

    user = CreatableSlugRelatedField(
        slug_field='email',
        queryset=models.UserModel.objects.all()
    )


class DepositorSerializer(EntitySerializer):

    class Meta:

        model = models.DepositorModel

        exclude = ('contract',)


class TrusteeSerializer(EntitySerializer):

    class Meta:

        model = models.TrusteeModel

        exclude = ('contract',)


class ContractSerializer(serializers.ModelSerializer):

    depositors = DepositorSerializer(many=True)

    trustees = TrusteeSerializer(many=True, allow_empty=False)

    read_only_fields = ('contract_address', 'time_created',
                        'time_update', 'status')

    def create(self, validated_data):
        """"
        1. removes depositors & trustee from dict
        2. loop through to add all depositors & trustees amount
        3. optimize by caching in a List (do not hit db)
        4. check if amounts are equal (total deposit == total withdrawal)
        """

        depositors: Dict = validated_data.pop('depositors', [])

        trustees: Dict = validated_data.pop("trustees", [])

        contract: models.ContractModel = models.ContractModel(
            **validated_data)

        depositors_model: List[models.DepositorModel] = []

        total_deposit_amount = 0

        for depositor in depositors:

            total_deposit_amount += depositor['amount']

            depositor['contract'] = contract

            depositors_model.append(models.DepositorModel(**depositor))

        else:

            total_deposit_amount = contract.amount

        total_trustee_amount = 0

        trustees_model: List[models.TrusteeModel] = []

        for trustee in trustees:

            total_trustee_amount += trustee['amount']

            trustee['contract'] = contract

            trustees_model.append(models.TrusteeModel(**trustee))

        if not (total_trustee_amount == total_deposit_amount and
                total_deposit_amount == contract.amount):

            raise serializers.ValidationError(
                {_("detail"): _('total amount not equal')})

        contract.save()

        models.DepositorModel.objects.bulk_create(depositors_model)

        models.TrusteeModel.objects.bulk_create(trustees_model)

        return contract

    class Meta:

        model = models.ContractModel

        fields = '__all__'
