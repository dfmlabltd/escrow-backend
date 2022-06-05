from rest_framework import serializers
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str


class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get_or_create(**{self.slug_field: data})
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field,
                      value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, obj):
        return getattr(obj, self.slug_field)


class EntitySerializer(serializers.ModelSerializer):

    user = CreatableSlugRelatedField(
        slug_field='email'
    )


class DepositorSerializer(EntitySerializer):

    class Meta:

        model = models.DepositorModel

        fields = '__all__'


class TrusteeSerializer(EntitySerializer):

    class Meta:

        model = models.TrusteeModel

        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):

    depositors = DepositorSerializer(many=True)

    trustees = TrusteeSerializer(many=True)

    class Meta:

        model = models.ContractModel

        fields = '__all__'
