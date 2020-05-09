from django.shortcuts import render
from .models import State, Hospital, Update
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response
from django.db.models import Count
from django.shortcuts import get_object_or_404

class Dashboard(TemplateResponseMixin, View):
    model = Hospital 
    template_name = 'dashboard.html'

    def get(self, request):
        profile = Hospital.objects.filter(owner=request.user)
        updates = Update.objects.filter(hospital=profile[0])
        update = updates[0]

        print(updates)
        print(update)

        return self.render_to_response({'profile': profile[0], 
                                        'updates': updates,
                                        'update': update})

class HospitalListView(TemplateResponseMixin, View):
    model = Hospital 
    template_name = 'list.html'

    def get(self, request, state=None, hospital=None):
        states = State.objects.annotate(
                    total_hospitals=Count('hospital'))
        hospitals = Hospital.objects.annotate(
                            total_updates=Count('update'))
        updates = Update.objects.filter(hospital=hospital)

        if state:
            state = get_object_or_404(State, slug=state)
            hospitals = hospitals.filter(state=state)
        #for i in hospitals:
        #   print(i)
        #   for update in updates:
        #       if(update.hospital==i):
        #            print(update)

        return self.render_to_response({'states': states,
                                        'state': state,
                                        'hospitals': hospitals,
                                        'updates': updates})                    

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'detail.html'

