# forms.py
from django import forms
from django_quill.forms import QuillFormField
from Library.models import MensajeBiblioteca
from django.conf import settings

# Define un campo personalizado para aceptar config_name
class CustomQuillFormField(QuillFormField):
    def __init__(self, *args, **kwargs):
        config_name = kwargs.pop('config_name', 'default')  # Usa 'default' si no se especifica otro
        self.config = settings.QUILL_CONFIGS.get(config_name, settings.QUILL_CONFIGS['default'])
        super().__init__(*args, **kwargs)

class MensajeBibliotecaForm(forms.ModelForm):
    mensaje = CustomQuillFormField(config_name='restricted')  # Usa configuración 'restricted'

    class Meta:
        model = MensajeBiblioteca
        fields = ('mensaje',)
