# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.timezone import now
class Paciente(models.Model):
	maxLen = 128
	#declaracion de tus campos
	nombreP = models.CharField(max_length=maxLen, null=False, unique=True)
	class Meta:
		pass
	def __str__(self):
		return self.nombreP
	def __unicode__(self):
		return self.__str__()

class Medico(models.Model):
	maxLen = 128
	#declaracion de tus campos
	nombreM = models.CharField(max_length=maxLen, null=False, unique=True)
	class Meta:
		pass
	def __str__(self):
		return self.nombreM
	def __unicode__(self):
		return self.__str__()
	def save(self, *args, **kwargs):
		#self.catSlug = slugify(self.catName)
		super(Medico, self).save(*args, **kwargs)

class Receta(models.Model):
	maxLen = 128
	#declaracion de tus campos
	medico = models.ForeignKey(Medico, null=False)
	paciente = models.ForeignKey(Paciente, null=False)
	class Meta:
		pass
	def __str__(self):
		return str(self.medico) + " " + str(self.paciente)
	def __unicode__(self):
		return self.__str__()
	def save(self, *args, **kwargs):
		#your code goes here
		super(Receta, self).save(*args, **kwargs)

