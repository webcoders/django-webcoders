from django import forms
from django.template import loader, Context
from django.utils.safestring import mark_safe


class DateWidget(forms.widgets.TextInput):
    class Media:
        css = {
            'all': ('css/datepicker3.css',)
        }
        js = ('js/bootstrap-datepicker.js',)

    def render(self, name, value, attrs=None):
        res = super(DateWidget, self).render(name, value, attrs)
        return mark_safe(u"""
    <div id="input-date-%s" class="input-group date" data-date-language="ru" data-date-format="dd.mm.yyyy">
        %s
        <span class="input-group-addon"><i class="glyphicon glyphicon-th"></i></span>
        <script>
            $('#input-date-%s').datepicker({});
        </script>
    </div>"""%(name, res, name))

class PhoneWidget(forms.widgets.TextInput):
     class Media:
        js = ('js/helpers/bootstrap-formhelpers-phone.js',)


class AddressWidget(forms.widgets.TextInput):
    class Media:
        js = (
              'js/ajax.js',
              )
    def render(self, name, value, attrs=None):
        res = super(AddressWidget, self).render(name, value, attrs)
        return mark_safe(u"""
    %s
    <script>
        $('#id_%s').typeahead({
            source: function (query, process) {
                return $.post('/webcoders/widgets/address/', { 'input':$( "#id_%s").val() }, function (data) {
                    return process(data.options);
                });
            }
        });
    </script>"""%(res, name, name))
