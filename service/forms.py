from django.forms import ModelForm

from service.models import MailingListSettings, Client


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class MailingListSettingsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MailingListSettings
        exclude = ('owner',)


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'name', 'comment', ]
