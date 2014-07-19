from django.forms.models import ModelForm
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils import six
from django.utils.translation import ugettext as _

class BootstrapFormFieldsetsMixin(object):

    fieldsets = None

    def as_bootstrap(self):
        html_class_attr='form-group'
        return self.__html_output__(
            normal_row = u'<div class="form-group %(extra_styles)s">%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="help-text">%s</div>',
            errors_on_separate_row = False)


    def __html_output__(self, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row):
        if self.fieldsets is None or type(self.fieldsets) not in (tuple, list):
            return self._html_output(self, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row)

        top_errors = self.non_field_errors() # Errors that should be displayed above all fields.
        output, hidden_fields = [], []

        for field in self.fieldsets:
            fieldset_name, fields = field
            output.append('<legend>%s</legend>'%fieldset_name)
            fields = fields['fields']
            for field in fields:
                if type(field) in (list, tuple):
                    i=0;
                    for _field in field:
                        res = self.__field_output__(_field, normal_row, errors_on_separate_row, error_row, help_text_html, offset=i)
                        i+=1;
                        output+=res
                        if i not in (0, len(field)):
                            output.append('<div class="form-group col-lg-1"></div>')
                elif type(field) in (str, unicode):
                    res = self.__field_output__(field, normal_row, errors_on_separate_row, error_row, help_text_html)
                    output+=res
        return mark_safe('\n'.join(output))

    def  __field_output__(self, _field, normal_row, errors_on_separate_row, error_row, help_text_html, offset=None):
        output = []
        extra_styles = ''
        html_class_attr = ''
        bf = self[_field]
        field = bf.field
        bf_errors = self.error_class([conditional_escape(error) for error in bf.errors])
        css_classes = bf.css_classes()
        if css_classes:
            html_class_attr = ' class="%s"' % css_classes

        if errors_on_separate_row and bf_errors:
            output.append(error_row % force_text(bf_errors))

        if bf.label:
            label = conditional_escape(force_text(bf.label))
            label = bf.label_tag(label) or ''
        else:
            label = ''

        if field.help_text:
            help_text = help_text_html % force_text(field.help_text)
        else:
            help_text = ''

        if offset is None:
            extra_styles = ' col-lg-12'
        else:
            extra_styles = ' col-lg-3'
        output.append(normal_row % {
            'extra_styles': extra_styles,
            'errors': force_text(bf_errors),
            'label': force_text(label),
            'field': six.text_type(bf),
            'help_text': help_text,
            'html_class_attr': html_class_attr
        })
        return output



class ModelForm(BootstrapFormFieldsetsMixin, ModelForm):
    pass