from rest_framework.routers import DefaultRouter

from commons.common import views


router = DefaultRouter()
router.register(
    r'counties', views.CountyViewSet, basename='county')
router.register(
    r'sub_counties', views.SubCountyViewSet, basename='sub_county')
router.register(
    r'constituencies', views.ConstituencyViewSet, basename='constituency')
router.register(
    r'divisions', views.DivisionViewSet, basename='division')
router.register(
    r'locations', views.LocationViewSet, basename='location')
router.register(
    r'sub_locations', views.SubLocationViewSet, basename='sub_location')
