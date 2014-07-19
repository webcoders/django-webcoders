from django import forms

from webcoders.forms.widgets import DateWidget, PhoneWidget, AddressWidget


base_css_class = 'form-control'

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')


class FieldAttrsMixin(object):
    def __init__(self, *args, **kwargs):
        super(FieldAttrsMixin, self).__init__(*args, **kwargs)
        self.widget.attrs['class'] = base_css_class;
        self.widget.attrs['placeholder'] = self.label;


class AddressField(FieldAttrsMixin, forms.CharField):

    widget = AddressWidget

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(AddressField, self).__init__(max_length, min_length, *args, **kwargs)
        self.widget.attrs['data-provide'] = 'typeahead';


class PhoneField(FieldAttrsMixin, forms.CharField):

    widget = PhoneWidget

    def __init__(self, max_length=None, min_length=None, input_format="+7 (ddd) ddd-dd-dd",  *args, **kwargs):
        super(PhoneField, self).__init__(max_length, min_length, *args, **kwargs)
        self.widget.attrs['class'] = self.widget.attrs['class'] + ' bfh-phone';
        self.widget.attrs['data-format'] = input_format

class DateField(FieldAttrsMixin, forms.DateField):
    widget = DateWidget
class URLField(FieldAttrsMixin, forms.URLField):
    pass
class EmailField(FieldAttrsMixin, forms.EmailField):
    pass
class TextField(FieldAttrsMixin, forms.CharField):
    pass
class CharField(FieldAttrsMixin, forms.CharField):
    pass;
class IntegerField(FieldAttrsMixin, forms.IntegerField):
    pass;
class ChoiceField(FieldAttrsMixin, forms.ChoiceField):
    pass;
