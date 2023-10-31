from django.urls import path

from service.views import MailingListSettingsListView, ClientListView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, ClientDetailView, MailingListSettingsCreateView, MailingListSettingsDetailView, \
    MailingListSettingsDeleteView, MailingListSettingsUpdateView, LogListView, change_mailing_status
from service.apps import ClientConfig

app_name = ClientConfig.name

urlpatterns = [
    path('', MailingListSettingsListView.as_view(), name='mailing_list'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),

    path('create_mail/', MailingListSettingsCreateView.as_view(), name='create_list'),
    path('view_mail/<int:pk>/', MailingListSettingsDetailView.as_view(), name='mail_view'),
    path('delete_mail/<int:pk>/', MailingListSettingsDeleteView.as_view(), name='delete_mail'),
    path('edit_mail/<int:pk>/', MailingListSettingsUpdateView.as_view(), name='edit_mail'),

    path('logs/', LogListView.as_view(), name='logs'),

    path('change_status/<int:pk>/', change_mailing_status, name='change_status'),

]
