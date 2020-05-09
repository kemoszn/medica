from django.contrib import admin
from .models import Update, Hospital, State

class UpdateInline(admin.StackedInline):
    model = Update

class HospitalInline(admin.StackedInline):
    model = Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    list_filter = ['state']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'state']
    inlines = [UpdateInline]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HospitalInline]


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ['masks', 'gloves', 'ventilators', 
                    'respirators']
    
