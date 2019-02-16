import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proyecto.settings')
import django
django.setup()
from aplicacion.models import Medico, Paciente, Receta
from random import randint
from django.core.files import File

def medico(idd, nombre):
	p = Medico.objects.get_or_create(id=idd, nombreM = nombre)[0]
	p.save()
	return p

def paciente(idd, nombre):
	p = Paciente.objects.get_or_create(id=idd, nombreP = nombre)[0]
	p.save()
	return p

def receta(idd, medicoID, pacienteID):
	medico = Medico.objects.filter(id=medicoID)[0]
	paciente = Paciente.objects.filter(id=pacienteID)[0]
	p = Receta.objects.get_or_create(id=idd, medico=medico, paciente=paciente)[0]
	p.save()
	return p

def populate():
	for i in xrange(1,5):
		medico(i, "medico"+str(i))
	for i in xrange(1,3):
		paciente(i, "paciente"+str(i))

	receta(1,1,1)
	receta(2,2,1)
	receta(3,1,2)
	receta(4,2,2)
	receta(5,3,2)

# Start execution here!
if __name__ == '__main__':
	print("Starting Shop population script...")
	populate()