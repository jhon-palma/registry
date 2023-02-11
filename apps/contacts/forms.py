from django import forms
from .choices import *
from .models import Agreements, Contacts, Urbanization, UrbanizationLeader
import django.forms.widgets

# DATE_INPUT_FORMATS = ('%d-%m-%Y')

# class DateInput(forms.DateInput):
#     input_type = 'date'
#     input_formats=DATE_INPUT_FORMATS

class NewContactForm(forms.ModelForm):
       
    class Meta:
        model = Contacts
        fields = '__all__'

        first_name = forms.CharField(max_length=50, label="Nombres",widget= forms.TextInput(attrs= {'placeholder':"Nombres"}))
        last_name = forms.CharField(max_length=50, label="Apellidos",widget= forms.TextInput(attrs= {'placeholder':"Apellidos"}))
        type_document = forms.ChoiceField(choices=TYPE_DOCUMENT, label="Tipo de Documento")
        document = forms.IntegerField(label="Número de Documento",widget= forms.TextInput(attrs= {'placeholder':"Número de documento"}))
        birthday = forms.DateField(label="Fecha de Nacimiento",widget=django.forms.DateInput(format = '%Y/%m/%d',
                attrs={'placeholder': 'yyyy-mm-dd', 'class': 'date',}))
        gender = forms.ChoiceField(choices=GENDER, label="Genero")
        address = forms.CharField(max_length=200, label="Dirección",widget= forms.TextInput(attrs= {'placeholder':"Dirección"}))
        urbanization = forms.ModelChoiceField(queryset=Urbanization.objects.all().order_by('urbanization'),label="Barrio")
        email =forms.CharField(label="Email",widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
        cellphone = forms.IntegerField(label="Celular",widget= forms.TextInput(attrs= {'placeholder':"Número Celular"}))
        ocupation = forms.ChoiceField(choices=OCUPATION,label="Ocupación")
        skills = forms.ChoiceField(choices=SKILLS, label="Nivel Educativo")
        leader = forms.ModelMultipleChoiceField(queryset=Urbanization.objects.all(),widget=forms.SelectMultiple,label='Lider')
        note = forms.CharField(required=False,widget=forms.Textarea, label="Observaciones")

class AgreementsForm(forms.ModelForm):
    class Meta:
        model = Agreements
        fields = '__all__'
    