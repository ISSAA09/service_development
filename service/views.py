from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Blog
from service.forms import MailingListSettingsForm, ClientForm
from service.models import MailingListSettings, Client, Log
from service.utils import MailingListCacheMixin


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('service:client_list')
    extra_context = {
        'title': 'Создание пользователя'
    }


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('service:client_list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }

    def get_success_url(self):
        return reverse('service:view', args=[self.object.pk])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('service:client_list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Подробная информация о пользователе'
    }


class MailingListSettingsListView(LoginRequiredMixin, PermissionRequiredMixin, MailingListCacheMixin, ListView):
    model = MailingListSettings
    permission_required = 'service.view_mailinglistsettings'
    extra_context = {
        'title': 'Главная - Список рассылок'
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status=MailingListSettings.STARTED).count()
        context_data['clients_count'] = Client.objects.values_list("email").distinct().count()

        blog = Blog.objects.order_by("?")[:3]
        context_data['blog'] = blog

        return context_data


class MailingListSettingsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MailingListSettings
    form_class = MailingListSettingsForm
    permission_required = 'service.add_mailinglistsettings'
    success_url = reverse_lazy('service:mailing_list')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingListSettingsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = MailingListSettings
    permission_required = 'service.view_mailinglistsettings'
    extra_context = {
        'title': 'Подробная информация о рассылке'
    }

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class MailingListSettingsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailingListSettings
    success_url = reverse_lazy('service:mailing_list')
    permission_required = 'service.delete_mailinglistsettings'
    extra_context = {
        'title': 'Удаление рассылки'
    }

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class MailingListSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingListSettings
    form_class = MailingListSettingsForm
    permission_required = 'service.change_mailinglistsettings'
    success_url = reverse_lazy('service:mailing_list')
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class LogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Log
    permission_required = 'service.view_log'
    extra_context = {
        'title': 'Логи рассылок'
    }


@login_required
@permission_required('service.change_status')
def change_mailing_status(request, pk):
    mailing_list_item = get_object_or_404(MailingListSettings, pk=pk)

    if (mailing_list_item.status == MailingListSettings.STARTED
            or mailing_list_item.status == MailingListSettings.CREATED):
        mailing_list_item.status = MailingListSettings.COMPLETED
    else:
        mailing_list_item.status = MailingListSettings.CREATED

    mailing_list_item.save()

    return redirect(reverse('service:mailing_list'))
