from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from .forms import AgreementsForm, NewContactForm
from .models import Agreements, Contacts, Urbanization

from django.contrib.messages.views import SuccessMessageMixin

# def new_contact(request):

#     if request.method == 'POST':
#         form = NewContactForm(request.POST)
#         if form.is_valid():
#             if Contacts.objects.filter(document=request.POST['document']).exists():
#                 messages.warning(request, 'El contacto ya existe')
#             else:
#                 contact = Contacts()
#                 contact.first_name = request.POST['first_name']
#                 contact.last_name = request.POST['last_name']
#                 contact.type_document = request.POST['type_document']
#                 contact.document = request.POST['document']
#                 contact.birthday = request.POST['birthday']
#                 contact.gender = request.POST['gender']
#                 contact.address = request.POST['address']
#                 contact.urbanization = Urbanization.objects.get(pk= request.POST['urbanization'])
#                 contact.email = request.POST['email']
#                 contact.cellphone = request.POST['cellphone']
#                 contact.ocupation = request.POST['ocupation']
#                 contact.skills = request.POST['skills']
#                 contact.note = request.POST['note']
#                 contact.save()
#                 messages.success(request,'Registro ingresado correctamente')
#                 return HttpResponseRedirect('new_contact')
        
#     else:
#         form = NewContactForm()
 
#     return render(request,'contacts/new_contact.html', {'form': form})

class List_contacts(ListView):
    model = Contacts
    paginate_by = 10
    template_name = 'contacts/list_contacts.html'
    
# def edit_contact(request, pk):
    
#     contact = get_object_or_404(Contacts, id=pk)
#     form = NewContactForm(initial={'first_name':contact.first_name, 
#                                    'last_name':contact.last_name,
#                                    'type_document':contact.type_document,
#                                    'document':contact.document,
#                                    'birthday':contact.birthday,
#                                    'gender':contact.gender,
#                                    'address':contact.address,
#                                    'urbanization':contact.urbanization,
#                                    'email':contact.email,
#                                    'cellphone':contact.cellphone,
#                                    'ocupation':contact.ocupation,
#                                    'skills':contact.skills,
#                                    'note':contact.note,
                                   
#                                    })
    
#     if request.method == 'POST':
#         form = NewContactForm(request.POST)
#         if form.is_valid():
#         #     contact = Contacts()
#             contact.first_name = request.POST['first_name']
#             contact.last_name = request.POST['last_name']
#             contact.type_document = request.POST['type_document']
#             contact.document = request.POST['document']
#             contact.birthday = request.POST['birthday']
#             contact.gender = request.POST['gender']
#             contact.address = request.POST['address']
#             contact.urbanization = Urbanization.objects.get(pk= request.POST['urbanization'])
#             contact.email = request.POST['email']
#             contact.cellphone = request.POST['cellphone']
#             contact.ocupation = request.POST['ocupation']
#             contact.skills = request.POST['skills']
#             contact.note = request.POST['note']
#             contact.save()
#             contact.save_m2m()
#             messages.success(request,'Registro actualizado correctamente')
#             #return redirect('list_contacts')
            
#     # else:
#     #     form = NewContactForm()
 
#     return render(request,'contacts/edit_contact.html', {'form': form })

class CreateContact(SuccessMessageMixin, CreateView):
    model = Contacts
    form_class = NewContactForm
    template_name = 'contacts/new_contact.html'
    success_url = reverse_lazy('contacts:CreateContact')
    success_message = "Registro creado correctamente"

class EditContact(SuccessMessageMixin, UpdateView):
    model=Contacts
    fields = ['first_name','last_name','type_document','document','birthday','gender','address','urbanization','email','cellphone','ocupation','skills','note','leader' ]
    template_name = 'contacts/edit_contact.html'
    success_url = reverse_lazy('contacts:list_contacts')
    success_message = "Registro actualizado correctamente"

class NewAgreements(SuccessMessageMixin, CreateView):
    model = Agreements
    form = AgreementsForm()
    fields = '__all__'
    template_name = 'contacts/new_agreements.html'
    success_url = reverse_lazy('contacts:CreateContact')
    success_message = "Registro creado correctamente"

class ListAgreements(ListView):
    model = Agreements
    paginate_by = 10
    template_name = 'contacts/list_agreements.html'

class EditAgreements(SuccessMessageMixin, UpdateView):
    model=Agreements
    fields = '__all__'
    template_name = 'contacts/edit_agreements.html'
    success_url = reverse_lazy('contacts:ListAgreements')
    success_message = "Registro actualizado correctamente"