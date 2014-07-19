from django.db.models.fields import CharField, TextField, IntegerField
from django.db.models.fields import DateField

from webcoders.forms import fields


class AddressField(CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': fields.AddressField}
        defaults.update(kwargs)
        return super(AddressField, self).formfield(**defaults)

class DateField(DateField):
    def formfield(self, **kwargs):
        defaults = {'form_class': fields.DateField}
        defaults.update(kwargs)
        return super(DateField, self).formfield(**defaults)

class CharField(CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': fields.CharField}
        defaults.update(kwargs)
        return super(CharField, self).formfield(**defaults)

class IntegerField(IntegerField):

    def formfield(self, **kwargs):
        defaults = {'form_class': fields.IntegerField}
        defaults.update(kwargs)
        return super(IntegerField, self).formfield(**defaults)


class TextField(TextField):

    def formfield(self, **kwargs):
        defaults = {'form_class': fields.CharField}
        defaults.update(kwargs)
        return super(TextField, self).formfield(**defaults)
