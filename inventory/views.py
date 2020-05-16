from django.shortcuts import render
from .models import State, Hospital, Update
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response
from django.db.models import Count
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import StateCreationForm, HospitalCreationForm
from django.http import HttpResponseRedirect


class HospitalCreationView(CreateView):
    template_name = 'form.html'
    form_class = HospitalCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class StateCreationView(CreateView):
    template_name = 'form.html'
    form_class = StateCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Dashboard')

    def form_valid(self, form):
        result = super(AdminRegistrationView,
                    self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result

class Dashboard(TemplateResponseMixin, View):
    model = Hospital 
    template_name = 'dashboard.html'

    def get(self, request):
        profile = Hospital.objects.filter(owner=request.user)
        updates = Update.objects.filter(hospital=profile[0])
        update = updates[0]
        labels = []
        data = []
        data_1 = []

        queryset = updates.order_by('created')
        for case in queryset:
            labels.append(case.created.strftime('%d %B'))
            data.append(case.confirmed)

        for case in queryset:
            data_1.append(case.pui)
        print(labels)
        return self.render_to_response({'profile': profile[0], 
                                        'updates': updates,
                                        'update': update,
                                        'labels': labels,
                                        'data': data,
                                        'data_1': data_1})

class HospitalListView(TemplateResponseMixin, View):
    model = Hospital 
    template_name = 'list.html'

    def get(self, request, state=None, hospital=None):
        states = State.objects.annotate(
                    total_hospitals=Count('hospital'))
        hospitals = Hospital.objects.annotate(
                            total_updates=Count('update'))
        updates = Update.objects.all()

        if state:
            state = get_object_or_404(State, slug=state)
            hospitals = hospitals.filter(state=state)
        print(hospitals)
        print(updates)
        for i in hospitals:
            print(i)
            for m in updates:
                if m.hospital == i.name:
                    print(m)
                
           
        return self.render_to_response({'states': states,
                                        'state': state,
                                        'hospitals': hospitals,
                                        'updates': updates})                    

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'detail.html'


def StatsView(request):
    template = 'stats.html'
    context = {}


    return render(request, template, context)
