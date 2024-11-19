from django import forms
from Classes.models import *

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre_contenido','activa', 'invitacion_zoom_link', 'fecha_clase', 'inicio_clase', 'final_clase', 'video']
        widgets = {
            'nombre_contenido': forms.TextInput(attrs={'class': 'form-control'}),
            'invitacion_zoom_link': forms.URLInput(attrs={'class': 'form-control'}),
            'fecha_clase': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'inicio_clase': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'final_clase': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'activa': forms.CheckboxInput(attrs={'class':'form-check-input', 'type':'checkbox'}),
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields =  '__all__' #['confirmacion', 'motivo_ausencia']
        widgets = {
            'id_asistencia': forms.HiddenInput(),  # Campo oculto
            'clase_asistencia': forms.HiddenInput(),  # Campo oculto
            #'asignatura_alumno': forms.HiddenInput(),  # Campo oculto
            'confirmacion': forms.CheckboxInput(attrs={'class':'form-check-input', 'type':'checkbox'}),  
            'motivo_ausencia': forms.TextInput(attrs={'class': 'form-control'}),
        }
