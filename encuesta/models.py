from django.db import models
from django.utils import timezone

class pregunta(models.Model):
	pregunta1=models.CharField(max_length=200)
	fecha=models.DateTimeField('fecha publicada')
	def __unicode__(self):
		return self.pregunta1

	def reciente(self):
		return self.fecha >= timezone.now()-timezone.timedelta(days=1)

class campo(models.Model):
	pregunta=models.ForeignKey(pregunta)
	campo_texto=models.CharField(max_length=200)
	votos=models.IntegerField(default=0)

	def __unicode__(self):
		return self.campo_texto
# Create your models here.
