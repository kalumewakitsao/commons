from rest_framework.viewsets import ModelViewSet

from commons.common import filters
from commons.common import models
from commons.common import serializers


class CountyViewSet(ModelViewSet):
    queryset = models.County.objects.all()
    filterset_class = filters.CountyFilter
    serializer_class = serializers.CountySerializer


class SubCountyViewSet(ModelViewSet):
    queryset = models.SubCounty.objects.all()
    filterset_class = filters.SubCountyFilter
    serializer_class = serializers.SubCountySerializer


class ConstituencyViewSet(ModelViewSet):
    queryset = models.Constituency.objects.all()
    filterset_class = filters.ConstituencyFilter
    serializer_class = serializers.ConstituencySerializer


class DivisionViewSet(ModelViewSet):
    queryset = models.Division.objects.all()
    filterset_class = filters.DivisionFilter
    serializer_class = serializers.DivisionSerializer


class LocationViewSet(ModelViewSet):
    queryset = models.Location.objects.all()
    filterset_class = filters.LocationFilter
    serializer_class = serializers.LocationSerializer


class SubLocationViewSet(ModelViewSet):
    queryset = models.SubLocation.objects.all()
    filterset_class = filters.SubLocationFilter
    serializer_class = serializers.SubLocationSerializer
