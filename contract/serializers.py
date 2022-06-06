from rest_framework import serializers
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str


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

    trustees = TrusteeSerializer(many=True)

    read_only_fields = ('contract_address', 'time_created',
                        'time_update', 'status')

    def create(self, validated_data):

        depositors = validated_data.pop('depositors', [])

        trustees = validated_data.pop("trustees", [])

        contract = models.ContractModel.objects.create(**validated_data)

        for depositor in depositors:

            depositor['contract'] = contract

            models.DepositorModel.objects.create(**depositor)

        for trustee in trustees:

            trustee['contract'] = contract

            models.TrusteeModel.objects.create(**trustee)

        return contract

    class Meta:

        model = models.ContractModel

        fields = '__all__'
