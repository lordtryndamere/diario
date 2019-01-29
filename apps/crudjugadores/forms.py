from django import forms
from apps.crudjugadores.models import Jugador

class JugadorForm(forms.ModelForm):
	class Meta:
		model = Jugador
		fields = [
			'id',
			'nombres',
			'apellidos',
			'fecha_nacimiento',
			'email',
			'deporte',
		]

		labels = {
			'id': 'Identificacion',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'fecha_nacimiento': 'Fecha de Nacimiento',
			'email': 'Correo Electronico',
			'deporte': 'Deporte',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'deporte': forms.Select(attrs={'class':'form-control'}),
		}