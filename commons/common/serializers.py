from django.utils import timezone
from rest_framework.serializers import ModelSerializer

from commons.common import models


class CommonSerializer(object):
    def create(self, validated_data):
        validated_data['created'] = timezone.now()
        validated_data['updated'] = timezone.now()

        user = self.context['request'].user
        if user:
            validated_data['created_by'] = user.guid
            validated_data['updated_by'] = user.guid
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['updated'] = timezone.now()

        user = self.context['request'].user
        if user:
            validated_data['updated_by'] = user.guid
        return super(CommonSerializer, self).update(instance, validated_data)


class CommonModelSerializer(CommonSerializer, ModelSerializer):

    class Meta:
        pass


class CountySerializer(CommonModelSerializer):

    class Meta:
        model = models.County
        fields = "__all__"


class SubCountySerializer(CommonModelSerializer):

    class Meta:
        model = models.SubCounty
        fields = "__all__"


class ConstituencySerializer(CommonModelSerializer):

    class Meta:
        model = models.Constituency
        fields = "__all__"


class DivisionSerializer(CommonModelSerializer):

    class Meta:
        model = models.Division
        fields = "__all__"


class LocationSerializer(CommonModelSerializer):

    class Meta:
        model = models.Location
        fields = "__all__"


class SubLocationSerializer(CommonModelSerializer):

    class Meta:
        model = models.SubLocation
        fields = "__all__"
