from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models.common_fields import Ledger, Timestamp


class Supplier(Timestamp):
    supplier_full_name = models.CharField(max_length=100, verbose_name=_('Supplier Full Name'))
    supplier_address = models.CharField(max_length=100, verbose_name=_('Supplier Address'))
    supplier_phone = PhoneNumberField()
    supplier_email = models.EmailField(unique=True, verbose_name=_('Supplier Email'))
    supplier_zip_code = models.CharField(max_length=10)
    supplier_country = CountryField()
    supplier_fax = models.BigIntegerField(null=True, blank=True, verbose_name=_('Supplier Fax'))
    supplier_previous_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Supplier Previous Balance'))

    supplier_ledger = models.ForeignKey(Ledger, on_delete=models.DO_NOTHING)

    def __str__(self):
        """String for representing the Model object."""
        return self.supplier_name + ' - ' + self.supplier_email