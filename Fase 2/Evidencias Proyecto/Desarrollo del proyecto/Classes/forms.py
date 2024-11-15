from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre_contenido', 'invitacion_zoom_link','fecha_clase', 'inicio_clase', 'final_clase']  # Excluir 'asignatura'
        widgets = {
            'fecha_clase': forms.DateInput(attrs={'type': 'date'}),
            'inicio_clase': forms.TimeInput(attrs={'type': 'time'}),
            'final_clase': forms.TimeInput(attrs={'type': 'time'}),
        }
