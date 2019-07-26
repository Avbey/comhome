from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, UpdateView,  TemplateView, DeleteView, DetailView)
from catalog.models import Address, Services
from catalog.forms import AddressForm, ServicesForm


class AddressesListView(LoginRequiredMixin, TemplateView):
    model = Address
    context_object_name = "addresses_list"
    template_name = "catalog/list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AddressesListView, self).get_context_data(**kwargs)
        context["addresses_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class AddressAddView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name = "catalog/create.html"

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        address_object = form.save(commit=False)
        address_object.created_by = self.request.user
        address_object.save()
        if self.request.POST.get("savenewform"):
            return redirect("catalog:address_add")
        else:
            return redirect("catalog:addresses_list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(AddressAddView, self).get_context_data(**kwargs)
        context["address_form"] = context["form"]
        return context


class AddressEditView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = "catalog/create.html"

    def get_form_kwargs(self):
        kwargs = super(AddressEditView, self).get_form_kwargs()
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        account_object = form.save(commit=False)
        account_object.save()
        return redirect("catalog:addresses_list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(AddressEditView, self).get_context_data(**kwargs)
        context["address_obj"] = self.object
        context["address_form"] = context["form"]
        return context


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'catalog/list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("catalog:addresses_list")


class ServicesListView(LoginRequiredMixin, TemplateView):
    model = Services
    context_object_name = "services_list"
    template_name = "catalog/list_service.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        context["services_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class ServiceAddView(LoginRequiredMixin, CreateView):
    model = Services
    form_class = ServicesForm
    template_name = "catalog/create_service.html"

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        service_object = form.save(commit=False)
        service_object.created_by = self.request.user
        service_object.save()
        if self.request.POST.get("savenewform"):
            return redirect("catalog:service_add")
        else:
            return redirect("catalog:services_list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(ServiceAddView, self).get_context_data(**kwargs)
        context["service_form"] = context["form"]
        return context


class ServiceEditView(LoginRequiredMixin, UpdateView):
    model = Services
    form_class = ServicesForm
    template_name = "catalog/create_service.html"

    def get_form_kwargs(self):
        kwargs = super(ServiceEditView, self).get_form_kwargs()
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        account_object = form.save(commit=False)
        account_object.save()
        return redirect("catalog:services_list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(ServiceEditView, self).get_context_data(**kwargs)
        context["services_obj"] = self.object
        context["service_form"] = context["form"]
        return context


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = 'catalog/list_service.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("catalog:services_list")


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Services
    context_object_name = "service"
    template_name = "catalog/detail_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.service = Services.objects.all()
        return super(ServiceDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        return context
