import uuid

from django.db import models
from django.utils import timezone

# https://stackoverflow.com/questions/53391715/django-errorname-is-not-defined-when-i-try-to-create-a-new-model  # noqa
# https://docs.djangoproject.com/en/2.1/topics/i18n/translation/
from django.utils.translation import gettext as _


# **********************************************************************************************#
'''
A definition of base for all models
'''


class Common(models.Model):
    """The Base Model for all models.
    This is the base model for all the models in this web application,
    containing fields explained below:
        `guid`: A globally unique field for all the objects inside
        the application.
        `created`: A datetime when a particular object was created.
        `created_by`: A guid of the user who created this particular object.
        `updated`: A datetime when a particular object was updated last.
        `updated_by`: A guid of the user who last updated the object.
        `owner`: The owner of this particular data object, will be used
        when the system advancesinto separating band data.
    """
    guid = models.UUIDField(
        editable=False, primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(
        db_index=True, default=timezone.now, blank=True, null=True)
    created_by = models.UUIDField(blank=True, null=True)
    updated = models.DateTimeField(
        db_index=True, default=timezone.now, blank=True, null=True)
    updated_by = models.UUIDField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-updated', '-created')


# **********************************************************************************************#
'''
A definition of common choices
'''


class Choices(Common):
    name = models.CharField(_("Name of the option"), max_length=100, unique=True)
    description = models.TextField(_("Description of the option"))

    class Meta:
        abstract = True


# **********************************************************************************************#
'''
A definition of common StatusLog models for models that transition states
'''


class StatusLog(Common):
    user_guid = models.UUIDField(
        _("GUID of the user perfoming the status bump"))
    user_name = models.CharField(
        _("Name of the user who bumped status"), max_length=100)
    description = models.TextField(_("Any extra description"))

    class Meta:
        abstract = True


# **********************************************************************************************#
'''
A definition of country as common data that will be required
'''


class County(models.Model):
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    county_code = models.CharField(
        _("Identifies the county code"), max_length=50, unique=True)
    county_name = models.CharField(
        _("Name of the county"), max_length=100)
    province = models.CharField(
        _("Province that a county belongs to"), max_length=100)


class SubCounty(models.Model):
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    sub_county_code = models.CharField(
        _("Code of the sub county"), max_length=50)
    county = models.ForeignKey(
        County, verbose_name=_("county"), on_delete=models.PROTECT)
    name = models.CharField(_("Name of the sub county"), max_length=100)


class Constituency(models.Model):
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    sub_county = models.ForeignKey(
        SubCounty, verbose_name=_("sub_county"), on_delete=models.PROTECT)
    name = models.CharField(_("Name of the constituency"), max_length=100)


class Division(models.Model):
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    constituency = models.ForeignKey(
        Constituency, verbose_name=_("constituency"), on_delete=models.PROTECT)
    name = models.CharField(_("Name of the division"), max_length=100)


class Location(models.Model):
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    division = models.ForeignKey(
        Division, verbose_name=_("division"), on_delete=models.PROTECT)
    name = models.CharField(_("Name of the location"), max_length=100)


class SubLocation(models.Model):
    '''
    If we store this on the address then we can get the whole tree
    '''
    guid = models.UUIDField(
        _("guid as a primary key"), primary_key=True, default=uuid.uuid4)
    location = models.ForeignKey(
        Location, verbose_name=_("location"), on_delete=models.PROTECT)
    name = models.CharField(_("Name of the sub location"), max_length=100)
