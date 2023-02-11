from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    # path('new_contact', views.new_contact, name='new_contact'),
    #path('<pk>/update_contact', views.edit_contact, name='edit_contact'),
    path('create_contacts', views.CreateContact.as_view(), name='CreateContact'),
    path('list_contacts', views.List_contacts.as_view(), name='ListContacts'),
    path('<pk>/EditContact', views.EditContact.as_view(), name='EditContact'),
    path('new_agreements', views.NewAgreements.as_view(), name='NewAgreements'),
    path('list_agreements', views.ListAgreements.as_view(), name='ListAgreements'),
    path('<pk>/EditAgreements', views.EditAgreements.as_view(), name='EditAgreements'),
]