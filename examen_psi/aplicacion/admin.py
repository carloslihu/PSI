# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Medico, Paciente, Receta

class MedicoAdmin(admin.ModelAdmin):
	prepopulated_fields = {}
	list_display = ('nombreM',)

# Add in this class to customise the Admin Interface
class PacienteAdmin(admin.ModelAdmin):
	prepopulated_fields = {}
	list_display = ('nombreP',)

class RecetaAdmin(admin.ModelAdmin):
	prepopulated_fields = {}
	list_display = ('id','medico','paciente')

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Receta, RecetaAdmin)

# Register your models here.
