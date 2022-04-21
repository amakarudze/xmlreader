from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Upload


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["file"]

    file = forms.FileField(label=_("Upload File"), allow_empty_file=True)
