from django.db import models
from django.contrib.auth.models import User 


class Filma(models.Model):
	izenburua = models.CharField(max_length=60)
	zuzendaria = models.CharField(max_length=60)
	urtea = models.IntegerField(max_length=11)
	generoa = models.CharField(max_length=2)
	sinopsia = models.CharField(max_length=700)
	bozkak = models.IntegerField(max_length=11)

	def __unicode__(self):
		return self.izenburua


class Bozkatzailea(models.Model):
	erabiltzailea_id = models.ForeignKey(User, on_delete=models.CASCADE)
	gogokofilmak = models.ManyToManyField(Filma)

	def __unicode__(self):
		return unicode(self.erabiltzailea_id)
