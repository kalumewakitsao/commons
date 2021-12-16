from django_filters.rest_framework import FilterSet

from commons.common import models


class CountyFilter(FilterSet):

    class Meta:
        model = models.County
        fields = "__all__"


class SubCountyFilter(FilterSet):

    class Meta:
        model = models.SubCounty
        fields = "__all__"


class ConstituencyFilter(FilterSet):

    class Meta:
        model = models.Constituency
        fields = "__all__"


class DivisionFilter(FilterSet):

    class Meta:
        model = models.Division
        fields = "__all__"


class LocationFilter(FilterSet):

    class Meta:
        model = models.Location
        fields = "__all__"


class SubLocationFilter(FilterSet):

    class Meta:
        model = models.SubLocation
        fields = "__all__"